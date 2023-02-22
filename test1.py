import sys
import subprocess

try:
    # 없는 모듈 import시 에러 발생
    import pandas
except:
    # pip 모듈 업그레이드
    subprocess.check_call([sys.executable,'-m', 'pip', 'install', '--upgrade', 'pip'])
    # 에러 발생한 모듈 설치
    subprocess.check_call([sys.executable,'-m', 'pip', 'install', '--upgrade', 'pandas'])
    # 다시 import
    import pandas
    