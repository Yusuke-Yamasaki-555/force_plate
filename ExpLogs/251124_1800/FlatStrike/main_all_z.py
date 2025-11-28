import csv
from itertools import zip_longest

def main():
    file_title_1 = "20251124204338"
    file_title_2 = "20251124204942"
    file_title_3 = "20251124205540"
    file_title_4 = "20251124210054"
    file_title_5 = "20251124210705"
    file_title_6 = "20251124211254"
    file_title_7 = "20251124211844"
    file_title_8 = "20251124212435"
    file_title_9 = "20251124213028"
    file_title_10 = "20251124213624"
    file_path_1L = './1/'+file_title_1+'_L.csv'
    file_path_1R = './1/'+file_title_1+'_R.csv'
    file_path_2L = './2/'+file_title_2+'_L.csv'
    file_path_2R = './2/'+file_title_2+'_R.csv'
    file_path_3L = './3/'+file_title_3+'_L.csv'
    file_path_3R = './3/'+file_title_3+'_R.csv'
    file_path_4L = './4/'+file_title_4+'_L.csv'
    file_path_4R = './4/'+file_title_4+'_R.csv'
    file_path_5L = './5/'+file_title_5+'_L.csv'
    file_path_5R = './5/'+file_title_5+'_R.csv'
    file_path_6L = './6/'+file_title_6+'_L.csv'
    file_path_6R = './6/'+file_title_6+'_R.csv'
    file_path_7L = './7/'+file_title_7+'_L.csv'
    file_path_7R = './7/'+file_title_7+'_R.csv'
    file_path_8L = './8/'+file_title_8+'_L.csv'
    file_path_8R = './8/'+file_title_8+'_R.csv'
    file_path_9L = './9/'+file_title_9+'_L.csv'
    file_path_9R = './9/'+file_title_9+'_R.csv'
    file_path_10L = './10/'+file_title_10+'_L.csv'
    file_path_10R = './10/'+file_title_10+'_R.csv'
    output_path = 'output.csv'

    try:
        # ファイルを開く (with文を使うことで自動的にcloseされます)
        with open(file_path_1L, mode='r', encoding='utf-8', newline='') as f1L, \
             open(file_path_1R, mode='r', encoding='utf-8', newline='') as f1R, \
             open(file_path_2L, mode='r', encoding='utf-8', newline='') as f2L, \
             open(file_path_2R, mode='r', encoding='utf-8', newline='') as f2R, \
             open(file_path_3L, mode='r', encoding='utf-8', newline='') as f3L, \
             open(file_path_3R, mode='r', encoding='utf-8', newline='') as f3R, \
             open(file_path_4L, mode='r', encoding='utf-8', newline='') as f4L, \
             open(file_path_4R, mode='r', encoding='utf-8', newline='') as f4R, \
             open(file_path_5L, mode='r', encoding='utf-8', newline='') as f5L, \
             open(file_path_5R, mode='r', encoding='utf-8', newline='') as f5R, \
             open(file_path_6L, mode='r', encoding='utf-8', newline='') as f6L, \
             open(file_path_6R, mode='r', encoding='utf-8', newline='') as f6R, \
             open(file_path_7L, mode='r', encoding='utf-8', newline='') as f7L, \
             open(file_path_7R, mode='r', encoding='utf-8', newline='') as f7R, \
             open(file_path_8L, mode='r', encoding='utf-8', newline='') as f8L, \
             open(file_path_8R, mode='r', encoding='utf-8', newline='') as f8R, \
             open(file_path_9L, mode='r', encoding='utf-8', newline='') as f9L, \
             open(file_path_9R, mode='r', encoding='utf-8', newline='') as f9R, \
             open(file_path_10L, mode='r', encoding='utf-8', newline='') as f10L, \
             open(file_path_10R, mode='r', encoding='utf-8', newline='') as f10R, \
             open(output_path, mode='w', encoding='utf-8', newline='') as f_out:

            reader1L = csv.reader(f1L)
            reader1R = csv.reader(f1R)
            reader2L = csv.reader(f2L)
            reader2R = csv.reader(f2R)
            reader3L = csv.reader(f3L)
            reader3R = csv.reader(f3R)
            reader4L = csv.reader(f4L)
            reader4R = csv.reader(f4R)
            reader5L = csv.reader(f5L)
            reader5R = csv.reader(f5R)
            reader6L = csv.reader(f6L)
            reader6R = csv.reader(f6R)
            reader7L = csv.reader(f7L)
            reader7R = csv.reader(f7R)
            reader8L = csv.reader(f8L)
            reader8R = csv.reader(f8R)
            reader9L = csv.reader(f9L)
            reader9R = csv.reader(f9R)
            reader10L = csv.reader(f10L)
            reader10R = csv.reader(f10R)
            writer = csv.writer(f_out)

            # zip_longest は長い方のリストに合わせてループします
            # fillvalue=None とすることで、短い方のデータが尽きたら None が返るようにします

            row_num = [1]

            for row1, \
                row2, \
                row3, \
                row4, \
                row5, \
                row6, \
                row7, \
                row8, \
                row9, \
                row10,  \
                row11, \
                  row12, \
                    row13, \
                      row14, \
                        row15, \
                          row16, \
                            row17, \
                              row18, \
                                row19, \
                                  row20  \
                    in zip_longest(reader1L, \
                                   reader1R, \
                                          reader2L, \
                                          reader2R, \
                                          reader3L, \
                                          reader3R, \
                                          reader4L, \
                                          reader4R, \
                                          reader5L, \
                                          reader5R, \
                                          reader6L, \
                                          reader6R, \
                                          reader7L, \
                                          reader7R, \
                                          reader8L, \
                                          reader8R, \
                                          reader9L, \
                                          reader9R, \
                                          reader10L, \
                                          reader10R, \
                                          fillvalue=None):

                # --- 1つ目のファイルの処理 (1-3列目) ---
                if row1 is None:
                    # 行が尽きている場合: 0埋め
                    data1 = ['0']
                else:
                    # 先頭3列を取得 (スライス機能)
                    data1 = row1[3]
                    # データ自体が3列未満だった場合の0埋め
                    # while len(data1) < 3:
                    #     data1.append('0')

                # --- 2つ目のファイルの処理 (4-6列目) ---
                if row2 is None:
                    # 行が尽きている場合: 0埋め
                    data2 = ['0']
                else:
                    # 先頭3列を取得
                    data2 = row2[3]
                    # データ自体が3列未満だった場合の0埋め
                    # while len(data2) < 3:
                    #     data2.append('0')
                
                if row3 is None:
                    data3 = ['0']
                else:
                    data3 = row3[3]

                if row4 is None:
                    data4 = ['0']
                else:
                    data4 = row4[3]
                
                if row5 is None:
                    data5 = ['0']
                else:
                    data5 = row5[3]

                if row6 is None:
                    data6 = ['0']
                else:
                    data6 = row6[3]

                if row7 is None:
                    data7 = ['0']
                else:
                    data7 = row7[3]

                if row8 is None:
                    data8 = ['0']
                else:
                    data8 = row8[3]

                if row9 is None:
                    data9 = ['0']
                else:
                    data9 = row9[3]

                if row10 is None:
                    data10 = ['0']
                else:
                    data10 = row10[3]

                if row11 is None:
                    data11 = ['0']
                else:
                    data11 = row11[3]

                if row12 is None:
                    data12 = ['0']
                else:
                    data12 = row12[3]

                if row13 is None:
                    data13 = ['0']
                else:
                    data13 = row13[3]

                if row14 is None:
                    data14 = ['0']
                else:
                    data14 = row14[3]

                if row15 is None:
                    data15 = ['0']
                else:
                    data15 = row15[3]

                if row16 is None:
                    data16 = ['0']
                else:
                    data16 = row16[3]

                if row17 is None:
                    data17 = ['0']
                else:
                    data17 = row17[3]

                if row18 is None:
                    data18 = ['0']
                else:
                    data18 = row18[3]

                if row19 is None:
                    data19 = ['0']
                else:
                    data19 = row19[3]

                if row20 is None:
                    data20 = ['0']
                else:
                    data20 = row20[3]

                # 結合して書き込み
                writer.writerow(row_num + data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data10 + data11 + data12 + data13 + data14 + data15 + data16 + data17 + data18 + data19 + data20)

                row_num[0] = row_num[0] + 1

        print(f"処理が完了しました: {output_path}")

    except FileNotFoundError as e:
        print(f"エラー: ファイルが見つかりません - {e}")
    except Exception as e:
        print(f"予期せぬエラーが発生しました: {e}")

if __name__ == "__main__":
    main()
