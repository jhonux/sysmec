from datetime import datetime, time, timedelta
from time import sleep
import os
from venv import logger
from db import get_db_conn
import querys


def main():
    logger.info('Iniciando rotina')
    # calcula as datas
    data_i = datetime.combine(datetime.today(), time.min) - timedelta(days=1)
    data_f = datetime.combine(datetime.today(), time.max) - timedelta(days=1)

    con = get_db_conn()
    cur = con.cursor()

    cur.execute(query_equipamentos.format(data_f))

    for row in cur.fetchall():
        equipamento = row[0]

        cur.execute(query_latencia, {'data_i': data_i, 'data_f': data_f, 'equipamentos': equipamento})
        resultado = cur.fetchall()

        cur.execute(insert_latencia, {'generic_id': resultado[0], 'data': data_i, 'avg': resultado[1]})

        con.commit()

    cur.close()
    con.close()

    return

if __name__ == '__main__':
    while True:
        data = date.today()
        main(data.month - 1, data.year)
        main(data.month - 2, data.year)
        main(data.month - 3, data.year)
        main(data.month - 4, data.year)
        
        data_proximo_mes = (datetime(data.year, data.month, 1) + timedelta(days=32)).replace(day=1)
        try:
            sleep((data_proximo_mes - datetime.now()).total_seconds())
        except ValueError:
            pass