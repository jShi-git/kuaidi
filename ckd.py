# -*- coding:utf-8 -*-

import requests, sys, json, time

ExpressList = {	'ems':'EMS',
				'shentong':'申通快递',
				'shunfeng':'顺丰速运',
				'yuantong':'圆通速递',
				'yunda':'韵达快运',
				'zhongtong':'中通快递',
				'huitongkuaidi':'汇通快运',
				'tiantian':'天天快递',
				'zhaijisong':'宅急送',
				'youzhengguonei':'邮政国内包裹',
				'youzhengguoji':'邮政国际包裹',
				'emsguoji':'EMS国际快递',
				'aae':'AAE-中国',
				'anjiekuaidi':'安捷快递',
				'anxindakuaixi':'安信达',
				'youzhengguonei':'包裹/平邮/挂号信',
				'bht':'BHT国际快递',
				'baifudongfang':'百福东方',
				'cces':'CCES（希伊艾斯）',
				'lijisong':'成都立即送',
				'dhl':'DHL',
				'dhlde':'DHL德国',
				'dsukuaidi':'D速物流',
				'debangwuliu':'德邦物流',
				'datianwuliu':'大田物流',
				'dpex':'DPEX',
				'disifang':'递四方',
				'ems':'EMS - 国内',
				'emsguoji':'EMS - 国际',
				'ems':'E邮宝',
				'rufengda':'凡客',
				'fedexus':'FedEx - 美国',
				'fedex':'FedEx - 国际',
				'lianbangkuaidi':'FedEx - 国内',
				'feikangda':'飞康达',
				'youzhengguonei':'挂号信',
				'ganzhongnengda':'能达速递',
				'gongsuda':'共速达',
				'gls':'GLS',
				'tiantian':'海航天天',
				'huitongkuaidi':'汇通快运',
				'tiandihuayu':'华宇物流',
				'hengluwuliu':'恒路物流',
				'haiwaihuanqiu':'海外环球',
				'huaxialongwuliu':'华夏龙',
				'jiajiwuliu':'佳吉快运',
				'jialidatong':'嘉里大通',
				'jiayiwuliu':'佳怡物流',
				'jinguangsudikuaijian':'京广速递',
				'jindawuliu':'金大物流',
				'jinyuekuaidi':'晋越快递',
				'jixianda':'急先达',
				'jiayunmeiwuliu':'加运美',
				'kuaijiesudi':'快捷速递',
				'lianbangkuaidi':'联邦快递',
				'longbanwuliu':'龙邦速递',
				'lanbiaokuaidi':'蓝镖快递',
				'lijisong':'立即送',
				'lejiedi':'乐捷递',
				'lianhaowuliu':'联昊通',
				'minghangkuaidi':'民航快递',
				'meiguokuaidi':'美国快递',
				'menduimen':'门对门',
				'ocs':'OCS',
				'quanfengkuaidi':'全峰快递',
				'quanyikuaidi':'全一快递',
				'quanchenkuaidi':'全晨快递',
				'quanjitong':'全际通',
				'quanritongkuaidi':'全日通',
				'rufengda':'如风达',
				'shentong':'申通E物流',
				'shentong':'申通快递',
				'shunfeng':'顺丰速运',
				'suer':'速尔快递',
				'shenghuiwuliu':'盛辉物流',
				'shengfengwuliu':'盛丰物流',
				'shangda':'上大国际',
				'santaisudi':'三态速递',
				'haihongwangsong':'山东海红',
				'saiaodi':'赛澳递',
				'tnt':'TNT',
				'tiantian':'天天快递',
				'tiandihuayu':'天地华宇',
				'tonghetianxia':'通和天下',
				'ups':'UPS',
				'usps':'USPS（美国邮政）',
				'wanjiawuliu':'万家物流',
				'wanxiangwuliu':'万象物流',
				'weitepai':'微特派',
				'xinhongyukuaidi':'鑫飞鸿',
				'xinbangwuliu':'新邦物流',
				'xinfengwuliu':'信丰物流',
				'cces':'希伊艾斯（CCES）',
				'yuantong':'圆通速递',
				'yunda':'韵达快运',
				'youzhengguonei':'邮政国内包裹',
				'youzhengguoji':'邮政国际包裹',
				'ems':'邮政特快专递',
				'yuanchengwuliu':'远成物流',
				'yafengsudi':'亚风速递',
				'yuanweifeng':'源伟丰',
				'youshuwuliu':'优速快递',
				'yuanzhijiecheng':'元智捷诚',
				'yuefengwuliu':'越丰物流',
				'yuananda':'源安达',
				'yuanfeihangwuliu':'原飞航',
				'yinjiesudi':'银捷速递',
				'yuntongkuaidi':'运通中港',
				'zhaijisong':'宅急送',
				'zhongtong':'中通快递',
				'zhongtiewuliu':'中铁快运',
				'ztky':'中铁物流',
				'zhongyouwuliu':'中邮物流',
				'zhimakaimen':'芝麻开门',
				'zhongxinda':'忠信达',
				'zhengzhoujianhua':'郑州建华'	}

Status = {	'0':'运输中...',
			'1':'已揽收',
			'2':'疑难件',
			'3':'已签收',
			'4':'已退回',
			'5':'派送中',
			'6':'退回中'	}

UrlBase = 'http://www.kuaidi100.com/query?type=%s&postid=%s';
error = ['Unknown error!'];

def run():
	if len(sys.argv) != 3:
		print 'Usage: ckd shunfeng 19968574'
	else:
		Request = requests.get(UrlBase % (sys.argv[1], str(sys.argv[2])))
		if Request.status_code == 200:
			PJSON = json.loads(Request.content)
			status = PJSON.get('status', -1)
			if status == -1:
				print error[0]
			else:
				if status == '200':
					print '=============================='
					print ('快递公司: ' + ExpressList.get(sys.argv[1], -1)).decode('utf8')
					print ('运 单 号: ' + sys.argv[2]).decode('utf8')
					print ('状　　态: ' + Status.get(PJSON.get('state', error[0]), error[0])).decode('utf8')
					print '=============================='
					for Item in PJSON.get('data', [{'time':time.strftime('%Y-%m-%d %H:%M:%S'), 'context':error[0]}]):
						print '[' + Item.get('time', error[0]) + ']	' + Item.get('context', error[0])
				else:
					print '====================Error!===================='
					print PJSON.get('message', error[0])
		quit();

if __name__ == '__main__':
	run()
