course_id = 'EACD-01FUND'
github_repo = 'UDEA-Esp-Analitica-y-Ciencia-de-Datos/%s'%course_id
zip_file_url="https://github.com/%s/archive/master.zip"%github_repo

def get_last_modif_date(localdir):
    try:
        import time, os, pytz
        import datetime
        k = datetime.datetime.fromtimestamp(max(os.path.getmtime(root) for root,_,_ in os.walk(localdir)))
        localtz = datetime.datetime.now(datetime.timezone(datetime.timedelta(0))).astimezone().tzinfo
        k = k.astimezone(localtz)
        return k
    except Exception:
        return None
    
import requests, zipfile, io, os, shutil
def init(force_download=False):
    if force_download or not os.path.exists("local"):
        print("replicating local resources")
        dirname = course_id+"-master/"
        if os.path.exists(dirname):
            shutil.rmtree(dirname)
        r = requests.get(zip_file_url)
        z = zipfile.ZipFile(io.BytesIO(r.content))
        z.extractall()
        if os.path.exists("local"):
            shutil.rmtree("local")
        shutil.move(dirname+"/local", "local")
        shutil.rmtree(dirname)

