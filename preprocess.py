import re
import jieba

def filter_and_segment(data):
    filter_pattern = r'[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）]+'
    
    filtered_data = []
    segmented_data = []
    
    for item in data:
        filtered_item = re.sub(filter_pattern, '', item)
        filtered_data.append(filtered_item)
        
        seg_list = jieba.cut(filtered_item)
        segmented_item = ' '.join(seg_list)
        segmented_data.append(segmented_item)
    
    return filtered_data, segmented_data

def count_words(segmented_data):
    word_count = {}
    
    for item in segmented_data:
        words = item.split(' ')
        for word in words:
            if word not in word_count:
                word_count[word] = 1
            else:
                word_count[word] += 1
    
    return word_count

# 读取txt文件
file_path = input("输入要进行处理的文件:")
with open(file_path, 'r', encoding='utf-8') as file:
    data = file.readlines()

# 去除换行符
data = [item.strip() for item in data]

# 过滤和分词处理
filtered_data, segmented_data = filter_and_segment(data)

# 分词统计
word_count = count_words(segmented_data)

# 按出现频次从大到小排序
sorted_word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

# 打印分词统计结果
with open('preprocessed_info.txt', 'w', encoding='utf-8') as output:
    for word, count in sorted_word_count:
        output.write(f"{word}: {count}\n")