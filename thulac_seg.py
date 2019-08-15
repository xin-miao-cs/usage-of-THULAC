import thulac

file_path = "E:/content.txt"  # 需要分词的数据集
out_path = "E:/content_seg.txt"  # 分词后的数据集


with open(file_path, 'r', encoding='utf-8') as fp:
    content = fp.read()
    thu = thulac.thulac()  # 默认模式,包词性标注
    seg = thu.cut(content)  # text=True返回的是str,text=False返回的是list,默认为False
    print(seg)  # [['今儿', 't'], ['个', 'q'], ['老百姓', 'n'], ['，', 'w'],
    # ['真', 'a'], ['呀', 'u'], ['真', 'd'], ['高兴', 'a'], ['！', 'w']]

    thu = thulac.thulac(seg_only=True)  # 只分词，不标注
    seg = thu.cut(content)
    print(seg)  # [['今儿', ''], ['个', ''], ['老百姓', ''], ['，', ''],
    # ['真', ''], ['呀', ''], ['真', ''], ['高兴', ''], ['！', '']]


thu = thulac.thulac()
seg = thu.cut_f(file_path, out_path)  # 直接将结果输出到文本中，但UTF-8格式无效，ANSI有效




