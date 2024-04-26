import requests
from lxml import etree

print('声明：输错东西程序会炸')
mc_version = input('请输入您的mc版本：')
print('版本：' + mc_version + '\n正在爬取推荐的forge和最新的forge...')
url = 'https://files.minecraftforge.net/net/minecraftforge/forge/index_' + mc_version + '.html'
get = requests.get(url).text
selector = etree.HTML(get)

recommended = selector.xpath('//html/body/main/div[2]/div[1]/div[2]/div/div[2]/div[1]/small/text()')
latest = selector.xpath('//html/body/main/div[2]/div[1]/div[2]/div/div[1]/div[1]/small/text()')

print('最新版：')
print(latest)
print('推荐版：')
print(recommended)
print('输入forge版本时不要把mc版本输进去')
forge_version = input('请输入forge版本：')

download_type = input('请输入下载类型（Installer、Changelog、Universal、Mdk、Src、Server、Client）：')

if download_type == 'Installer' or download_type == 'Universal':
    file_extensions = '.jar'

if download_type == 'Changelog':
    file_extensions = '.txt'

if download_type == 'Mdk' or download_type == 'Src' or download_type == 'Server' or download_type == 'Client':
    file_extensions = '.zip'

if download_type == 'Src':
    file_extensions = '.zip'

if download_type == 'Server':
    file_extensions = '.zip'

if download_type == 'Client':
    file_extensions = '.zip'

FILE_NAME = 'forge-' + mc_version + '-' + forge_version + '-' + download_type + file_extensions
file_name = FILE_NAME.lower()

DOWNLOAD_URL = 'https://maven.minecraftforge.net/net/minecraftforge/forge/' + mc_version + '-' + forge_version + '/forge-' + mc_version + '-' + forge_version + '-' + download_type + file_extensions
download_url = DOWNLOAD_URL.lower()

str_html = requests.get(download_url)
with open(file_name, 'wb') as f:
    f.write(str_html.content)
    input('下载成功（按回车键结束）')