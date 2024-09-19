# 画像のリンクを置いてるファイルの定義
csv_file = 'pic_list.csv'

# 画像リンク（お試し用）
filelink = 'https://photos.google.com/u/0/album/AF1QipN2f3csXsYYGGpJhVPzztz4Qi3-hs6DXA2uXLmD/photo/AF1QipOlXlqTewX8USCz390zUKVKwL6a_jMjWRKQSLjn?hl=ja'

# 画像をランダムに送信するcsvから画像IDをリスト化する関数
def get_picture_id(filepath):

    pic_id = {}    # 写真のIDを入れるリスト
    pic_num = 0 # 写真のリストの個数管理

    # CSVファイルを開く
    with open(filepath, 'r') as file:
        # ファイルを1行ずつ読み込む
        data_list = []
        for line in file:
            # 各行をカンマで区切り、リストに変換
            row = line.strip().split(',')
            data_list.append(row)
    
    # file（写真）であるもののIDだけ取得してpic_idに追加
    for i in range(len(data_list)):
        # csvに格納されたgoogleドライブの共有urlの読み出し
        url = data_list[i][0]
        # 写真のIDだけをpic_idリストに入れる
        if 'file' in url:
            url = url.replace('https://drive.google.com/file/d/', '')
            pic_id[pic_num] = url.replace('/view?usp=drivesdk','')
            pic_num += 1

    return pic_num,pic_id