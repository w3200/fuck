from weipinhui.zhuce import Zhuce
import unittest
import HTMLTestRunner
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart

if __name__ == '__main__':
    #先创建一个测试套件
    my_suite=unittest.TestSuite()
    #将SuanShuDanyanTest类中的所有用例加载到测试套件中
    # my_suite.addTests(unittest_baidu.TestLoader().loadTestsFromTestCase(SuanShuDanyanTest))
    #单个添加
    my_suite.addTest(Zhuce('test_zhuce'))
    my_suite.addTest(Zhuce('test_denglu'))
    my_suite.addTest(Zhuce('test_nanzhuang'))

    #创建 单元测试启动器
    # runner = unittest.TextTestRunner(verbosity=2)
    # runner.run(my_suite)

    #  定义生成测试报告的名称
    filename1="result.html"
    fp = open(filename1,'wb')
    # 定义测试报告的路径，标题，描述等内容
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'唯品会自动化测试报告',description=u'唯品会自动化测试报告')
    # 执行测试脚本，并生成测试报告
    runner.run(my_suite)


    # ------------------------发送邮件--------------------
    file_name = "result.html"
    sender = "783354786@qq.com"
    receivers = ["938662600@qq.com", "1542706542@qq.com","251266295@qq.com"]  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

    # 创建一个带附件的实例
    message = MIMEMultipart()
    message['From'] = Header("王亚鹏", 'utf-8')
    message['To'] = Header("测试经理", 'utf-8')
    subject = '唯品会的测试报告'
    message['Subject'] = Header(subject, 'utf-8')

    # 邮件正文内容
    message.attach(MIMEText('这是唯品会的测试报告，附件是具体报告！', 'plain', 'utf-8'))

    # 构造附件1，传送当前目录下的 test.txt 文件
    att1 = MIMEText(open(file_name, 'rb').read(), 'base64', 'utf-8')
    att1["Content-Type"] = 'application/octet-stream'
    # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
    att1["Content-Disposition"] = 'attachment; filename="result_weipinhui.html"'
    message.attach(att1)

    # # 构造附件2，传送当前目录下的 runoob.txt 文件
    # att2 = MIMEText(open('runoob.txt', 'rb').read(), 'base64', 'utf-8')
    # att2["Content-Type"] = 'application/octet-stream'
    # att2["Content-Disposition"] = 'attachment; filename="runoob.txt"'
    # message.attach(att2)

    try:
        smtpObj = smtplib.SMTP_SSL("smtp.qq.com", 465)
        smtpObj.login("783354786@qq.com", "nmztlsacahfobefg")  # 仅smtp服务器需要验证时
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("邮件发送成功")

    except smtplib.SMTPException:
        print("Error: 无法发送邮件")

