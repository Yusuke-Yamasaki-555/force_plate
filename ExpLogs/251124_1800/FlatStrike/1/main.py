import csv
from itertools import zip_longest

def main():
    file_title_1 = "20251124204338"
    file_title_2 = "20251124204338"
    file_title_3 = "20251124204338"
    file_title_4 = "20251124204338"
    file_title_5 = "20251124204338"
    file_title_6 = "20251124204338"
    file_title_7 = "20251124204338"
    file_title_8 = "20251124204338"
    file_title_9 = "20251124204338"
    file_title_10 = "20251124204338"
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
             open(file_path_1L, mode='r', encoding='utf-8', newline='') as f1L, \
             open(file_path_1R, mode='r', encoding='utf-8', newline='') as f1R, \
             open(file_path_1L, mode='r', encoding='utf-8', newline='') as f1L, \
             open(file_path_1R, mode='r', encoding='utf-8', newline='') as f1R, \
             open(file_path_1L, mode='r', encoding='utf-8', newline='') as f1L, \
             open(file_path_1R, mode='r', encoding='utf-8', newline='') as f1R, \
             open(file_path_1L, mode='r', encoding='utf-8', newline='') as f1L, \
             open(file_path_1R, mode='r', encoding='utf-8', newline='') as f1R, \
             open(file_path_1L, mode='r', encoding='utf-8', newline='') as f1L, \
             open(file_path_1R, mode='r', encoding='utf-8', newline='') as f1R, \
             open(file_path_1L, mode='r', encoding='utf-8', newline='') as f1L, \
             open(file_path_1R, mode='r', encoding='utf-8', newline='') as f1R, \
             open(file_path_1L, mode='r', encoding='utf-8', newline='') as f1L, \
             open(file_path_1R, mode='r', encoding='utf-8', newline='') as f1R, \
             open(file_path_1L, mode='r', encoding='utf-8', newline='') as f1L, \
             open(file_path_1R, mode='r', encoding='utf-8', newline='') as f1R, \
             open(file_path_1L, mode='r', encoding='utf-8', newline='') as f1L, \
             open(file_path_1R, mode='r', encoding='utf-8', newline='') as f1R, \
             open(output_path, mode='w', encoding='utf-8', newline='') as f_out:

            reader1 = csv.reader(f1)
            reader2 = csv.reader(f2)
            writer = csv.writer(f_out)

            # zip_longest は長い方のリストに合わせてループします
            # fillvalue=None とすることで、短い方のデータが尽きたら None が返るようにします
            for row1, row2 in zip_longest(reader1, reader2, fillvalue=None):
                
                # --- 1つ目のファイルの処理 (1-3列目) ---
                if row1 is None:
                    # 行が尽きている場合: 0埋め
                    data1 = ['0', '0', '0']
                else:
                    # 先頭3列を取得 (スライス機能)
                    data1 = row1[:3]
                    # データ自体が3列未満だった場合の0埋め
                    while len(data1) < 3:
                        data1.append('0')

                # --- 2つ目のファイルの処理 (4-6列目) ---
                if row2 is None:
                    # 行が尽きている場合: 0埋め
                    data2 = ['0', '0', '0']
                else:
                    # 先頭3列を取得
                    data2 = row2[:3]
                    # データ自体が3列未満だった場合の0埋め
                    while len(data2) < 3:
                        data2.append('0')

                # 結合して書き込み
                writer.writerow(data1 + data2)

        print(f"処理が完了しました: {output_path}")

    except FileNotFoundError as e:
        print(f"エラー: ファイルが見つかりません - {e}")
    except Exception as e:
        print(f"予期せぬエラーが発生しました: {e}")

if __name__ == "__main__":
    main()
