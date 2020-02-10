import io
import matplotlib.style as mplstyle
from gifconfig import *
from func_input import *
from gifmaker import *
from historylog import *
from preconfig import *
from functionsettings import *
from dialog import *
import sys

mplstyle.use('fast')

'''
在这里注明一下用到的第三方模块:
numpy,moviepy,matplotlib,pyqt5,imageio...
'''


def get_settings():
    setdata = {'duration': ui_set.duration.text(), 'fps': ui_set.fps.text()}
    detect_text(setdata, 'bk_color', ui_set.bk_color.text(), 'white')
    setdata['pic_size'] = ui_set.pic_size.text()
    setdata['gifname'] = ui_set.gif_name.text()
    setdata['storage_path'] = ui_set.storage_path.text()
    detect_text(setdata, 'precision', ui_set.precision.text(), '0.01')
    setdata['coo_range'] = ui_set.coo_range.text()
    setdata['m_range'] = ui_set.m_range.text()
    setdata['keep_track'] = ui_set.keep_track.isChecked()
    setdata['x_fm'] = ui_set.x_fm.toPlainText()
    setdata['y_gm'] = ui_set.y_gm.toPlainText()
    return setdata


def mainfun():
    ui_dia.plainTextEdit.appendPlainText(str(get_settings()))
    setdata = get_settings()
    coo_rangelist = data_to_list('coo_range', '-5,5,-5,5', setdata)
    pic_sizelist = data_to_list('pic_size', '6,6', setdata)
    m_rangelist = data_to_list('m_range', '-5,5', setdata)
    fig, ax1 = draw_fig(coo_rangelist[0], coo_rangelist[1], coo_rangelist[2], coo_rangelist[3],
                        pic_sizelist[0], pic_sizelist[1], setdata.get('bk_color', 'white'))  # 生成图片基本格式
    funclist = getfunctions(setdata)  # 接受用户输入的函数
    recvfunlist = funclist[0] + funclist[1]
    update_log_fun(setdata, recvfunlist)  # 更新日志
    ui_dia.plainTextEdit.appendPlainText('\nupdating finished')
    if ui_set.keep_track.isChecked() is True:
        logic2 = 'y'
    else:
        logic2 = ''
    try:
        t0, tl0 = get_time()  # 开始计时
        funclist[0], funclist[1] = makefunlist(funclist[0], funclist[1], setdata)  # 制作每一帧对应的函数表
        make_gif(fig, ax1, funclist, coo_rangelist, m_rangelist, setdata, logic2)  # 编译函数表并制作gif
        t1, tl1 = get_time()  # 计时结束
        ui_dia.plainTextEdit.appendPlainText('%ss' % (t1 - t0))  # 输出制作花费时间
        update_log_time(tl0, tl1)  # 更新日志
    except FileNotFoundError:
        ui_dia.plainTextEdit.appendPlainText('There is no such path to store picture.')
    except:
        ui_dia.plainTextEdit.appendPlainText('An unexcepted error has occured, you can get it in historylog.txt.')
        update_log_error()  # 在日志中记录错误
    else:
        ui_dia.plainTextEdit.appendPlainText('finish')


def click_button():  # 点击'make the gif'按钮,开始制作gif
    ui_dia.plainTextEdit.setPlainText('')
    ui_dia.progressBar.setValue(0)
    dialog.show()
    mainfun()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui_set = Ui_settings()  # 简化ui名称
    ui_dia = Ui_Dialog()
    settings = QtWidgets.QMainWindow()  # 简化窗口名称
    dialog = QtWidgets.QDialog()
    try:  # 读取本地存储设置
        preconfigdict = read_preconfig()
    except FileNotFoundError or io.UnsupportedOperation or TypeError:
        preconfigdict = write_preconfig_default()
    ui_set.setupUi(settings)  # 启动Ui界面
    ui_dia.setupUi(dialog)
    ui_set.storage_path.setText(preconfigdict['copy0'])  # 设置存储路径
    ui_set.bk_color.setText(preconfigdict['facecolor'])  # 设置背景颜色
    settings.show()
    ui_set.pushButton.clicked.connect(click_button)
    app.exec_()
