import csv
from itertools import zip_longest

def main():
    file_title = "20251124204338"
    file1_path = file_title+'_L.csv'
    file2_path = file_title+'_R.csv'
    output_path = 'output.csv'

    try:
        # ファイルを開く (with文を使うことで自動的にcloseされます)
        with open(file1_path, mode='r', encoding='utf-8', newline='') as f1, \
             open(file2_path, mode='r', encoding='utf-8', newline='') as f2, \
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
