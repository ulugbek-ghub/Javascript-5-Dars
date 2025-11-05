##pc0={
##    'ram':16,
##    'ssd':2048,
##    'gpu':gtx_1080
##    }
##pc1={
##    "chip":amd,
##    'ram':8,
##    'ssd':1024,
##    'gpu':radeon_rx7000
##    }
##pc2={
##    "chip":samsung,
##    'ram':64,
##    'ssd':4096,
##    'gpu':rtx_4090
##    }
##pcs=[pc0,pc1,pc2]
##for pc in pcs:
##    print(f"1-kompyuterimizda {pc[ram]}lik tezkor xotira,{pc[ssd]}]lik doimiy xotira va tezkor ishlashi uchun {pc[gpu]} videokartasi o'rnatilgan"
##          )

import calendar
yy=50080
mm=8
print(calendar.month(yy,mm))