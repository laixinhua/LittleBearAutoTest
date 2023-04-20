#存放相册权限页面元素
#要允许小竹熊访问您设备上的照片、媒体内容和文件吗？-允许
allow = '//android.widget.Button[1][text(),"允许"]'
#要允许小竹熊访问您设备上的照片、媒体内容和文件吗？-拒绝
refuse = '//*[starts-with(@text,"拒绝")]'
#要允许小竹熊拍摄照片和录制视频吗？-允许
allow1 = '//android.widget.Button[1][text(),"允许"]'
#要允许小竹熊拍摄照片和录制视频吗？-拒绝
refuse1 = '//*[starts-with(@text,"拒绝")]'
#要允许小竹熊录制音频吗？-允许
allow2 = '//android.widget.Button[1][text(),"允许"]'
#要允许小竹熊录制音频吗？-拒绝
refuse2 = '//*[starts-with(@text,"拒绝")]'
#要允许小竹熊访问您的通讯录吗？-允许
allow3 = '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.Button[1]'
#要允许小竹熊访问您的通讯录吗？-拒绝
refuse3 = '//*[starts-with(@text,"拒绝")]'
#音视频通话-要允许小竹熊录制音频吗？-允许
allow4 = '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.Button[2]'
#音视频通话-要允许小竹熊录制音频吗？-拒绝
refuse4 = '//*[starts-with(@text,"拒绝")]'
#音视频通话-要允许小竹熊拍摄照片和录制视频吗？-允许
allow5 = '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.Button[2]'
#音视频通话-要允许小竹熊拍摄照片和录制视频吗？-拒绝
refuse5 = '//*[starts-with(@text,"拒绝")]'
#聊天页-要允许小竹熊访问您设备上的照片、媒体内容和文件吗？-允许
allow6 = '//android.widget.Button[2][text(),"允许"]'
#聊天页-要允许小竹熊访问您设备上的照片、媒体内容和文件吗？-拒绝
refuse6 = '//*[starts-with(@text,"拒绝")]'

#语音通话-挂断
Hang_up = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[2]/android.widget.ImageView'
