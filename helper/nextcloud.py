import asyncio
import aiohttp
import xml.etree.ElementTree as ET

class nextcloud:
    upload_point = "https://dms.uom.lk/remote.php/webdav/"
    
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.islogged_in = False
        self.used_quota = None
        self.available_quota = None

    
    async def login(self):
        username = self.username
        password = self.password
        uploadpoint = nextcloud.upload_point

        headers = {
            'Depth': '1',  # Important: Tells WebDAV to list folder contents (not just the folder itself)
            'Content-Type': 'application/xml'
        }

        # This is the XML body that requests file properties
        xml_body = '''<?xml version="1.0" encoding="UTF-8"?>
        <d:propfind xmlns:d="DAV:" xmlns:oc="http://owncloud.org/ns" xmlns:nc="http://nextcloud.org/ns">
        <d:prop>
            <d:gxetlastmodified/>
            <d:getcontentlength/>
            <d:quota-available-bytes />
            <d:quota-used-bytes />
            <d:getcontenttype/>
            <oc:permissions/>
            <d:resourcetype/>
            <d:getetag/>
        </d:prop>
        </d:propfind>'''

        async with aiohttp.ClientSession() as session:
            async with session.request('PROPFIND', uploadpoint, data=xml_body,
                                    headers=headers,
                                    auth=aiohttp.BasicAuth(username, password)) as resp:
                response_text = await resp.text()
                root = ET.fromstring(response_text)
                ns = {
                    'd': 'DAV:',
                    'oc': 'http://owncloud.org/ns',
                    'nc': 'http://nextcloud.org/ns'
                }

                response = root.find('.//d:response', ns)
                if response is not None:
                    self.islogged_in = True
                    available_quota = response.find('.//d:quota-available-bytes', ns)
                    used_quota = response.find('.//d:quota-used-bytes', ns)
                    if available_quota is not None and used_quota is not None:
                        self.available_quota = int(available_quota.text)
                        self.used_quota = int(used_quota.text)
                    else:
                        print("Quota information not found in the response.")
                        return False

                if resp.status in [200, 201, 204,207]:
                    return True
                else:
                    print(f"Login failed with status {resp.status}: {response_text}")
                    return False
    
    
    async def upload(self,file_path,file_name):
        async with aiohttp.ClientSession() as session:
            with open(file_path, 'rb') as file:
                upload_url = f"{nextcloud.upload_point}{file_name}"
                async with session.put(upload_url, data=file,auth=aiohttp.BasicAuth(self.username,self.password)) as response:
                    if response.status in [200,201,204 ]:
                        return True
                    else:
                        print(f"Upload failed with status {response.status}")
                        return f"Upload failed with status {response.status}"
        
    def share(self,upload_path,):
        pass