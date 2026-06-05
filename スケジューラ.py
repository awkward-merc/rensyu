import time
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import timedelta
import sys

# スクリプトを終了するジョブ
def exit_program(sched):
	print(f'------{sys._getframe().f_code.co_name} 開始------')

	# raise KeyboardInterrupt("manual interrupt")
	# sys.exit()  # スクリプト全体を終了
	print(f'残りジョブ数：{len(sched.get_jobs())}')
	sched.shutdown(wait=False) #スケジューラを終了
	print(f"スクリプト終了: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
	
	print(f'------{sys._getframe().f_code.co_name} 終了------\n')

def mod(sched):
	print(f'------{sys._getframe().f_code.co_name} 開始------')

	# execTime=datetime.now() + timedelta(seconds=1)
# 	sched.add_job(mod, 'date', run_date=execTime + timedelta(seconds=1), args=[sched]) #時刻
# 	sched.add_job(mod, 'date', run_date=execTime + timedelta(seconds=2), args=[sched]) #時刻

	print(f'残りジョブ数：{len(sched.get_jobs())}')
	print("mod完了。時刻:%s" % datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

	print(f'------{sys._getframe().f_code.co_name} 終了------\n')

def main():	
	start = time.time()
	print(f'---{sys._getframe().f_code.co_name} 開始---')
	
	scheduler = BlockingScheduler() # スケジューラを作る

	execTime=datetime.now() + timedelta(seconds=1)

	scheduler.add_job(mod, 'interval', seconds=5, args=[scheduler])  # インターバル
	scheduler.add_job(mod, 'date', run_date=execTime + timedelta(seconds=2), args=[scheduler]) #時刻

	scheduler.add_job(exit_program, 'date', run_date=execTime + timedelta(seconds=30), args=[scheduler]) #時刻

	try:
		scheduler.start()
	except (KeyboardInterrupt, SystemExit):
		print('実行完了')
		pass
	
	print(f'---{sys._getframe().f_code.co_name} 終了---\n')
	print('所要時間：' + str(round(time.time() - start,2))+'秒')
	
if __name__ == "__main__":
	main()

