import csv
from itertools import zip_longest

def main():
  file_title_1  = "20251202103948"
  file_title_2  = "20251202104634"
  file_title_3  = "20251202105239"
  file_title_4  = "20251202105835"
  file_title_5  = "20251202110427"
  file_title_6  = "20251202111009"
  file_title_7  = "20251202111542"
  file_title_8  = "20251202112115"
  file_title_9  = "20251202112655"
  file_title_10 = "20251202113251"
  file_paths = [
      ('./1/'+file_title_1+'_L.csv', './1/'+file_title_1+'_R.csv'),
      ('./2/'+file_title_2+'_L.csv', './2/'+file_title_2+'_R.csv'),
      ('./3/'+file_title_3+'_L.csv', './3/'+file_title_3+'_R.csv'),  
      ('./4/'+file_title_4+'_L.csv', './4/'+file_title_4+'_R.csv'),
      ('./5/'+file_title_5+'_L.csv', './5/'+file_title_5+'_R.csv'),
      ('./6/'+file_title_6+'_L.csv', './6/'+file_title_6+'_R.csv'),
      ('./7/'+file_title_7+'_L.csv', './7/'+file_title_7+'_R.csv'),
      ('./8/'+file_title_8+'_L.csv', './8/'+file_title_8+'_R.csv'),
      ('./9/'+file_title_9+'_L.csv', './9/'+file_title_9+'_R.csv'),
      ('./10/'+file_title_10+'_L.csv', './10/'+file_title_10+'_R.csv')
  ]
  
  output_paths = [
      'output_1.csv',
      'output_2.csv',
      'output_3.csv',
      'output_4.csv',
      'output_5.csv',
      'output_6.csv',
      'output_7.csv',
      'output_8.csv',
      'output_9.csv',
      'output_10.csv'
  ]

  for (file_left, file_right), output in zip(file_paths, output_paths):

    print(f"処理中のファイル: {file_left} と {file_right}")
      

    try:
      # ファイルを開く (with文を使うことで自動的にcloseされます)
      with open(file_left, mode='r', encoding='utf-8', newline='') as f1, \
          open(file_right, mode='r', encoding='utf-8', newline='') as f2, \
          open(output, mode='w', encoding='utf-8', newline='') as f_out:

        reader1 = csv.reader(f1)
        reader2 = csv.reader(f2)
        writer = csv.writer(f_out)

        writer.writerow(['', 'Left_Z[N]', 'Right_Z[N]'])  # ヘッダー行を書く

        # zip_longest は長い方のリストに合わせてループします
        # fillvalue=None とすることで、短い方のデータが尽きたら None が返るようにします
        row_num = [1]
        for row1, row2 in zip_longest(reader1, reader2, fillvalue=None):
            
            # --- 1つ目のファイルの処理 (1-3列目) ---
          if row1 is None:
              # 行が尽きている場合: 0埋め
              data1 = ['0']
          else:
              # 先頭3列を取得 (スライス機能)
              data1 = row1[2]
              # データ自体が3列未満だった場合の0埋め
              # while len(data1) < 3:
              #     data1.append('0')

          # --- 2つ目のファイルの処理 (4-6列目) ---
          if row2 is None:
              # 行が尽きている場合: 0埋め
              data2 = ['0']
          else:
            # 先頭3列を取得
            data2 = row2[2]
            # データ自体が3列未満だった場合の0埋め
            # while len(data2) < 3:
            #     data2.append('0')

          # 結合して書き込み
          writer.writerow(row_num + [data1, data2])

          row_num[0] += 1
          if row_num[0]-1 > 15000:
              break

      print(f"処理が完了しました: {output}")

    except FileNotFoundError as e:
      print(f"エラー: ファイルが見つかりません - {e}")
    except Exception as e:
      print(f"予期せぬエラーが発生しました: {e}")

if __name__ == "__main__":
  main()
