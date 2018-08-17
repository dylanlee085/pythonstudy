1 #coding=utf-8
 2 from selenium import webdriver
 3 import os
 4 import time

 5 # set little time stop and big time stop for viewing changes
 6 little_time_stop = 1
 7 big_time_stop = 2
 8 # 默认广告条数
 9 ads_num_require = 8
10 # 请求连接
11 req_url = "http://www.haosou.com/s?ie=utf-8&shb=1&src=360sou_newhome&q=%E9%B2%9C%E8%8A%B1"
12 # 打开浏览器
13 
14 browser = webdriver.Chrome()
15 # 开始请求
16 17 browser.get(req_url)
18 # 获取所有的广告
19 
20 all_ads_li = browser.find_elements_by_css_selector('#e_idea_pp li')
21 # 当前广告条数
22 ads_num_current = len(all_ads_li)
23 print "Has been got %d ads" %(ads_num_current)
24 # 如果广告条数与默认不符
25 if ads_num_current < ads_num_require:
26     print "The number of ads is not enough ( current : %d require: %d)" %(ads_num_current,ads_num_require)
27     # exit()
28 # 获取顶部连接
29 i = 0
30 for ads_li in all_ads_li:
31     time.sleep(big_time_stop)
32     i = i+1
33     print "ads %d :" %i
34     try:
35         main = ads_li.find_element_by_css_selector('h3 a')
36     except:
37         print "\tError: ads %d cann't find" %(i)
38     else:
39         print "\tReady: visit ads %d" %(i)
40         main.click()
41         print "\tSucess: visit ads %d" %(i)
42         time.sleep(little_time_stop)
43     try:
44         img_link = ads_li.find_element_by_class_name('e_biyi_img')
45     except:
46         print "\tError : no img in ads %d " %(i)
47     else:
48         print "\tReady : visit img_link %d" %(i)
49         img_link.click()
50         print "\tSuccess : visit img_link %d" %(i)
51         time.sleep(little_time_stop)
52     try:
53         child_div = ads_li.find_element_by_class_name('e_biyi_childLink');
54     except:
55         print "\tError : no child link in ads %d" %(i)
56     else:
57         try:
58             child_links = child_div.find_elements_by_css_selector('a')
59         except:
60             print "\tError : find child_links error"
61         else:
62             num_links = len(child_links)
63             print "\tSuccess : there are %d child_links" %(num_links)
64             j = 0
65             for child_a in child_links:
66                 j = j + 1
67                 print "\t\tReady : visit child link %d in ads %d" %(j, i)
68                 child_a.click()
69                 print "\t\tSuccess : visit child link %d in ads %d" %(j, i)
70                 time.sleep(little_time_stop)
71 print "End and thanks for your using!"
72 # 下面代码选择取消注释
73 # 延时
74 # time.sleep(5)
75 # 关闭当前窗口
76 # browser.close()
77 # 关闭所有已经打开的窗口
78 # browser.quit()
