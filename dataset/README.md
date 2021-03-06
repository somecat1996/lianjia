# Dataset

 > described in `dataset.py`

```python
dataset(*, src='./data2', dst='./dataset', load_from_source=False)
```

 - Keyword arguments:
    * `src` -- `str`, source data path
    * `dst` -- `str`, dataset path
    * `load_from_source` -- `bool`, flag if load from source (`False` in default)

 - Returns:
    * `Dataset<Info>` -- parsed dataset (for more information, see notes below)
        ```
        (Info) Dataset
            |-- (int) id -- ID
            |-- (str) title -- 标题
            |-- (str) heading -- 副标题
            |-- (float) price -- 总价（单位为元）
            |-- (float) average -- 均价（单位为元/平米）
            |-- (Info) community -- 小区
            |       |-- (str) name -- 小区名称
            |       |-- (str) intro -- 小区介绍
            |-- (Info) region -- 所在区域
            |       |-- (int) district -- 行政区划编码
            |       |-- (str) station -- 所处地铁站辐射区
            |       |-- (str) ring -- 外中内环情况
            |-- (Info) type -- 房屋户型
            |       |-- (int) room -- 居室数量
            |       |-- (int) saloon -- 客厅数量
            |       |-- (int) kitchen -- 厨房数量
            |       |-- (int) bath -- 卫浴数量
            |-- (Info) floor -- 所在楼层
            |       |-- (int) level -- 高中低楼层或地下室
            |       |-- (int) total -- 总楼层数
            |-- (float) scale -- 建筑面积（单位为平方米）
            |-- (int) structure -- 户型结构
            |-- (float) area -- 套内面积（单位为平方米）
            |-- (int) building -- 建筑类型
            |-- (tuple<int>) orientation -- 房屋朝向
            |-- (int) framework -- 建筑结构
            |-- (Info) decoration -- 装修
            |       |-- (int) condition -- 装修情况
            |       |-- (str) description -- 装修描述
            |-- (Info) ratio -- 梯户比例
            |       |-- (int) lift -- 电梯数量
            |       |-- (int) apt -- 每层户数
            |-- (int) elevator -- 配备电梯
            |-- (int) title_term -- 产权年限
            |-- (datetime) listing_time -- 挂牌时间
            |-- (int) rights -- 交易权属
            |-- (datetime) last_transaction -- 上次交易
            |-- (int) purpose -- 房屋用途
            |-- (int) house_term -- 房屋年限
            |-- (int) ownership -- 产权所属
            |-- (Info) mortgage -- 抵押
            |       |-- (bool) flag -- 是否抵押
            |       |-- (tuple<str>) info -- 抵押信息
            |       |-- (str) comment -- 权属抵押
            |-- (int) deed -- 房本备件
            |-- (tuple<int>) tags -- 房源标签
            |-- (str) intro -- 房源标签
            |-- (str) facility -- 周边配套
            |-- (str) inspiration -- 核心卖点
            |-- (str) transport -- 交通出行
            |-- (str) detail -- 售房详情
            |-- (str) tax -- 税费解析
            |-- (str) suitable -- 适宜人群
            |-- (int) villa -- 别墅类型
            |-- (str) analysis -- 投资分析
        ```

    - Terminology:
        * `district` (行政区划编码):
            ```python
            DIVISION_CODE = {
                '黄埔' : 310101,
                '徐汇' : 310104,
                '长宁' : 310105,
                '静安' : 310106,
                '普陀' : 310107,
                '虹口' : 310109,
                '杨浦' : 310110,
                '闵行' : 310112,
                '宝山' : 310113,
                '嘉定' : 310114,
                '浦东' : 310115,
                '金山' : 310116,
                '松江' : 310117,
                '青浦' : 310118,
                '奉贤' : 310120,
                '崇明' : 310151,
            }
            ```
        * `level` (高中低楼层或地下室):
            ```python
            FLOOR_LEVEL = {
                '低' : 0,
                '中' : 1,
                '高' : 2,
                '地下室' : 4,
            }
            ```
        * `structure` (户型结构):
            ```python
            STRUCTURE_CODE = {
                '复式' : 0,
                '平层' : 1,
                '跃层' : 2,
                '错层' : 3,
            }
            ```
        * `building` (建筑类型):
            ```python
            BUILDING_TYPE = {
                '塔楼' : 0,
                '板楼' : 1,
            }
            ```
        * `orientation` (房屋朝向):
            ```python
            (
                0,  # 东
                0,  # 东南
                0,  # 南
                0,  # 西南
                0,  # 西
                0,  # 西北
                0,  # 北
                0,  # 东北
            )
            ```
        * `framework` (建筑结构):
            ```python
            FRAMEWORK_CODE = {
                '砖混结构' : 0,
                '钢混结构' : 1,
            }
            ```
        * `condition` (装修情况):
            ```python
            CONDITION_CODE = {
                '毛坯' : 0,
                '简装' : 1,
                '精装' : 2,
            }
            ```
        * `elevator` (配备电梯):
            ```python
            ELEVATOR_CODE = {
                '无' : 0,
                '有' : 1,
            }
            ```
        * `rights` (交易权属):
            ```python
            TRADING_RIGHTS = {
                '动迁安置房' : 0,
                '售后公房' : 1,
                '商品房' : 2,
            }
            ```
        * `purpose` (房屋用途):
            ```python
            PURPOSE_CODE = {
                '别墅': 0,
                '新式里弄': 1,
                '旧式里弄': 2,
                '普通住宅': 3,
                '老公寓': 4,
                '花园洋房': 5,
            }
            ```
        * `house_term` (房屋年限):
            ```python
            HOUSE_TERM = {
                '未满两年': 0,
                '满两年': 1,
                '满五年': 2,
            }
            ```
        * `ownership` (产权所属):
            ```python
            PROPERTY_OWNERSHIP = {
                '非共有' : 0,
                '共有' : 1,
            }
            ```
        * `deed` (房本备件):
            ```python
            DEED_CODE = {
                '未上传房本照片' : 0,
                '已上传房本照片' : 1,
            }
            ```
        * `tags` (房源标签):
            ```python
            (
                0,  # 房本满两年
                0,  # 房本满五年
                0,  # 随时看房
                0,  # 地铁
            )
            ```
        * `villa` (别墅类型):
            ```python
            VILLA_TYPE = {
                '联排': 0,
                '独栋': 1,
                '双拼': 2,
                '叠拼': 3,
            }
            ```
        * for `tuple` vecters, `0` for `False`, `1` for `True`
        * for `int` flags, `-1` for unexpected/unknown value
        * for `str` contents, `None` for empty fields

    - Notes:
        * `Info` turn dictionaries into object-like instances
            - inherits from `dict` type
            - iterable, and support all functions as `dict`
            - immutable, thus cannot set or delete attributes after initialisation
            - `infotodict` -- reverse `Info` object into `dict` type
        * `Dataset` object herits from `tuple`
            ```python
            # returns from `dataset` function
            >>> data = dataset()
            # subscriptable as normal tuples
            >>> data[0]
            >>> data[1:10]
            # or to fetch certain keys
            >>> data[1, 'apt', 'lift']
            Info(apt=(2,), lift=(1,))
            >>> data[1:3, 'price', 'average']
            Info(price=(2600000.0, 3080000.0), average=(44636, 36032))
            ```
