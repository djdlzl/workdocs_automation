import subprocess
import json
from datetime import datetime, timedelta
import pytz

# 시간대 설정
timezone = pytz.timezone("Asia/Seoul")

# maintenance_start_time 변수에 24시간 전 시간을 저장
maintenance_start_time = datetime.now(tz=timezone) - timedelta(hours=24)

# end_time 변수에 현재 시간을 저장
end_time = datetime.now(tz=timezone)

# AWS CLI 명령어 실행
cmd = f"aws cloudwatch get-metric-statistics --profile idlookmall --namespace AWS/ElastiCache \
--metric-name CPUUtilization \
--start-time {maintenance_start_time.strftime('%Y-%m-%dT%H:%M:%SZ')} \
--end-time {end_time.strftime('%Y-%m-%dT%H:%M:%SZ')} \
--period 300 \
--statistics Maximum \
--dimensions Name=CacheClusterId,Value=id-dev-an2-ec-a-redis Name=CacheNodeId,Value=0001"

result = subprocess.run(cmd, stdout=subprocess.PIPE, shell=True, encoding='utf-8')

if result.returncode != 0:
    print(f"Error running command {cmd}")
else:
    data = json.loads(result.stdout)

# 데이터 처리
count = 0

for datapoint in data['Datapoints']:
    if datapoint['Maximum'] >= 1:
        count += 1
        # 별도의 파일에 쓰기
        with open('redis001_over70.json', 'a') as output_f:
            output_f.write(f"{count}. ")
            json.dump(datapoint, output_f)
            output_f.write('\n')

