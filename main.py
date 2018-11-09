# -*- coding:utf-8 -*-
from etl.etl_service import EtlService
from threading import Thread

if __name__ == "__main__":
    etl_ser = EtlService(ip="127.0.0.1", port=8808)
    etl_ser.start()
    t = Thread(target=etl_ser.do_print, args=(etl_ser.get_q(),))
    t.start()
    etl_ser.join()

