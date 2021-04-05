# Mobile Device Model Data (移动设备型号数据文件)
记录、映射当前主流厂商「设备代号（Model）」到「产品名」映射，方便程序处理，定期更新。  

更新时间：2021-04-05

##### 格式：  
> 型号:名称:品牌

如：  
```txt
iPhone13,1:iPhone 12 Mini:Apple
iPhone13,2:iPhone 12:Apple
iPhone13,3:iPhone 12 Pro:Apple
iPhone13,4:iPhone 12 Pro Max:Apple
OCE-AN00:HUAWEI Mate 40E 全网通版:HUAWEI
OCE-AN10:HUAWEI Mate 40 全网通版:HUAWEI
NOH-AN00:HUAWEI Mate 40 Pro 全网通版:HUAWEI
NOP-AN00:HUAWEI Mate 40 Pro+ 全网通版:HUAWEI
NOP-AN00:HUAWEI Mate 40 RS 保时捷设计:HUAWEI
TAH-AN00:HUAWEI Mate X:HUAWEI
TAH-AN00m:HUAWEI Mate Xs:HUAWEI
TET-AN00 TET-AN10:HUAWEI Mate X2:HUAWEI
```

详见：[mobile.txt](./dist/mobile.txt)

##### 相关厂商：  
- 苹果 (Apple)
- 小米 (Xiaomi)
- 华为 (HUAWEI)
- 荣耀 (HONOR)
- vivo
- OPPO
- 三星 (Samsung)
- 一加 (OnePlus)
- 真我 (realme) 
- 魅族 (MEIZU) 
- 联想 (Lenovo)
- 摩托罗拉 (Motorola)
- 诺基亚 (Nokia)
- 中兴 (ZTE)
- 努比亚 (nubia)
- 乐视 (Letv) 
- 坚果 (Smartisan)
- 360 手机


## 使用方法
解析文件，用于转义设备名称

- Flask 样例： [server](./server/flask_demo.py) 

## 数据来源
 - 安卓设备：https://github.com/KHwang9883/MobileModels
 - iOS 设备：https://gist.github.com/adamawolf/3048717
 
 
## 许可

<a rel="license" href="https://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="知识共享许可协议" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />本作品采用 <a rel="license" href="https://creativecommons.org/licenses/by-nc-sa/4.0/">知识共享署名-非商业性使用-相同方式共享 4.0 国际许可协议</a> 进行许可。
