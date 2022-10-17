"""
if elif else语句的使用
"""
# height = int(input("请输入身高："))
# vip_level = int(input("请输入会员等级:"))
# if height < 120:
#     print("儿童免票")
# elif vip_level > 3:
#     print("高级会员，免票")
# else:
#     print("请前往售票处购票")

# 代码简化
if int(input("请输入身高:")) < 120:
    print("儿童免票")
elif int(input("请输入会员等级:")) > 3:
    print("高级会员，免票")
else:
    print("请前往售票处购票")