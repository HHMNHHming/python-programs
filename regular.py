import re

#首先要搞清楚各个正则的含义
# r (\w)  (\W) (|) ^  $ {4,8} 
#注意后面这个数字，要大于等于实际的长度
# (?P<name>)
# (?P=name)
content = '$#lianflower_@163.com'
ma = re.match(r'(\W+)(\w+)@(163|126).com',content)
print(ma.group(1))

me = re.search(r'(\w+)@(163|126).com',content)
print(me)
print(me.group())


qq = '11522342@qq.com*****'
match = re.match(r'^[\w]{4,8}@(163|qq).com(\W+)$',qq)
print(match)
print(match.group())

ma = re.match(r'[\w]{4,10}@(163|126).com', 'lianflower@163.com')	
print(ma.group())       # 输出：lianflower@163.com



ma = re.match(r'[\w]{4,10}@(163|126).com', 'lianflower@126.com')
print(ma.group())       # 输出：lianflower@126.com
 
 
 
# <number>	引用编号为number（数字）的分组所匹配到的字符串
# 例：匹配html标签的有效性
ma = re.match(r'<[\w]+>', '<book>')	
print(ma.group())       # 输出：<book>
 
ma = re.match(r'<([\w]+>)', '<book>')	# 注意这里分组匹配的范围为([w]+>) 没有左边的<	
print(ma.groups())      # 输出：('book>',)	# 当我们在正则表达式中使用()进行分组匹配时。
						# 那么我们可以使用groups以元组的形式输出匹配结果
 
ma = re.match(r'<([\w]+>)\1', '<book>book>')	# 1用来引用分组([w]+>)所匹配到的字符串book>
print(ma.group())       # 输出：<book>book>
 
ma = re.match(r'<([\w]+>)</\1', '<book></book>')# 在1前加上字符</就可以匹配出</book>
print(ma.group())       # 输出：<book></book>
 
ma = re.match(r'<([\w]+>)[\w]+</\1', '<book>python</book>')# 再加上[w]+后，可以匹配一个完整的html标签
print(ma.group())       # 输出：<book>python</book>
 
 
 
# (?P<name>)	为分组起一个别名（因为一个正则表达式中可能有多个分组，
		# 所以起个别名在引用的时候会比较方便）
 
# (?P=name)	引用名为name的分组所匹配到的字符串

print("\n") 
ma = re.match(r'<(?P<song>[\w]+>)[\w]+</(?P=song)', '<book>python</book>')
print(ma.group())       # 输出：<book>python</book>
			# (?P<song>[\w]+>)意思为：为分组([\w]+>)起一个别名为song
			# (?P=song)意思为：引用名为song的分组所匹配到的字符串
			# 为字符串起别名，然后用别名去调用字符串 (?P<name>)  (?P=name)
