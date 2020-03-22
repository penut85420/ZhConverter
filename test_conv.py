import unittest
from zhhanz_conv import ZhhanzMan
import php_conv

class TestCase(unittest.TestCase):
    def test_s2t(self):
        zm = ZhhanzMan()
        self.assertEqual(zm.trans_s2t('硬盘上无法修复的坏轨，'), '硬盤上無法修復的壞軌，')
        self.assertEqual(zm.trans_s2t('可能导致硬盘使用上产生异常的现象，'), '可能導致硬盤使用上產生異常的現象，')
        self.assertEqual(zm.trans_s2t('例如：存取缓慢、当机、档案毁损等症状发生。'), '例如：存取緩慢、當機、檔案毀損等症狀發生。')
        self.assertEqual(zm.trans_s2t('最近上市的固态硬盘也会使用广泛使用于 DRAM 内存的 ECC 技术来保护快闪存储器资料。'), '最近上市的固態硬盤也會使用廣泛使用於 DRAM 內存的 ECC 技術來保護快閃存儲器資料。')
        self.assertEqual(zm.trans_s2t('网志（英语：Blog）是一种由个人管理、张贴新的文章、图片或影片的网站或线上日记，'), '網誌（英語：Blog）是一種由個人管理、張貼新的文章、圖片或影片的網站或線上日記，')
        self.assertEqual(zm.trans_s2t('用来纪录、抒发情感或分享资讯。'), '用來紀錄、抒發情感或分享資訊。')
        self.assertEqual(zm.trans_s2t('网志上的文章通常根据张贴时间，'), '網誌上的文章通常根據張貼時間，')
        self.assertEqual(zm.trans_s2t('以倒序方式由新到旧排列。'), '以倒序方式由新到舊排列。')
        self.assertEqual(zm.trans_s2t('许多博客作者专注评论特定的课题或新闻，'), '許多博客作者專注評論特定的課題或新聞，')
        self.assertEqual(zm.trans_s2t('其他则作为个人日记。'), '其他則作為個人日記。')
        self.assertEqual(zm.trans_s2t('一个典型的博客结合了文字、图像、其他博客或网站的超连结、及其它与主题相关的媒体。'), '一個典型的博客結合了文字、圖像、其他博客或網站的超連結、及其它與主題相關的媒體。')
        self.assertEqual(zm.trans_s2t('能够让读者以互动的方式留下意见，'), '能夠讓讀者以互動的方式留下意見，')
        self.assertEqual(zm.trans_s2t('是许多博客的重要要素。'), '是許多博客的重要要素。')
        self.assertEqual(zm.trans_s2t('大部分的博客内容以文字为主，'), '大部分的博客內容以文字為主，')
        self.assertEqual(zm.trans_s2t('也有一些博客专注艺术、摄影、视频、音乐、播客等各种主题。'), '也有一些博客專注藝術、攝影、視頻、音樂、播客等各種主題。')
        self.assertEqual(zm.trans_s2t('网志是社会媒体网络的一部分。'), '網誌是社會媒體網絡的一部分。')
        self.assertEqual(zm.trans_s2t('皇后在后面吃面'), '皇后在後面吃麵')
        self.assertEqual(zm.trans_s2t('舰队Collection 是日本网络游戏'), '艦隊Collection 是日本網絡遊戲')
        self.assertEqual(zm.trans_s2t('是消歧义页面'), '是消歧義頁面')
        self.assertEqual(zm.trans_s2t('陈公乾生'), '陳公乾生')


    def test_t2s(self):
        zm = ZhhanzMan()
        self.assertEqual(zm.trans_t2s('硬盤上無法修復的壞軌，'), '硬盘上无法修复的坏轨，')
        self.assertEqual(zm.trans_t2s('可能導致硬盤使用上產生異常的現象，'), '可能导致硬盘使用上产生异常的现象，')
        self.assertEqual(zm.trans_t2s('例如：存取緩慢、當機、檔案毀損等症狀發生。'), '例如：存取缓慢、当机、档案毁损等症状发生。')
        self.assertEqual(zm.trans_t2s('最近上市的固態硬盤也會使用廣泛使用於 DRAM 內存的 ECC 技術來保護快閃存儲器資料。'), '最近上市的固态硬盘也会使用广泛使用于 DRAM 内存的 ECC 技术来保护快闪存储器资料。')
        self.assertEqual(zm.trans_t2s('網誌（英語：Blog）是一種由個人管理、張貼新的文章、圖片或影片的網站或線上日記，'), '网志（英语：Blog）是一种由个人管理、张贴新的文章、图片或影片的网站或线上日记，')
        self.assertEqual(zm.trans_t2s('用來紀錄、抒發情感或分享資訊。'), '用来纪录、抒发情感或分享资讯。')
        self.assertEqual(zm.trans_t2s('網誌上的文章通常根據張貼時間，'), '网志上的文章通常根据张贴时间，')
        self.assertEqual(zm.trans_t2s('以倒序方式由新到舊排列。'), '以倒序方式由新到旧排列。')
        self.assertEqual(zm.trans_t2s('許多博客作者專注評論特定的課題或新聞，'), '许多博客作者专注评论特定的课题或新闻，')
        self.assertEqual(zm.trans_t2s('其他則作為個人日記。'), '其他则作为个人日记。')
        self.assertEqual(zm.trans_t2s('一個典型的博客結合了文字、圖像、其他博客或網站的超連結、及其它與主題相關的媒體。'), '一个典型的博客结合了文字、图像、其他博客或网站的超连结、及其它与主题相关的媒体。')
        self.assertEqual(zm.trans_t2s('能夠讓讀者以互動的方式留下意見，'), '能够让读者以互动的方式留下意见，')
        self.assertEqual(zm.trans_t2s('是許多博客的重要要素。'), '是许多博客的重要要素。')
        self.assertEqual(zm.trans_t2s('大部分的博客內容以文字為主，'), '大部分的博客内容以文字为主，')
        self.assertEqual(zm.trans_t2s('也有一些博客專注藝術、攝影、視頻、音樂、播客等各種主題。'), '也有一些博客专注艺术、摄影、视频、音乐、播客等各种主题。')
        self.assertEqual(zm.trans_t2s('網誌是社會媒體網絡的一部分。'), '网志是社会媒体网络的一部分。')
        self.assertEqual(zm.trans_t2s('皇后在後面吃麵'), '皇后在后面吃面')
        self.assertEqual(zm.trans_t2s('艦隊Collection 是日本網絡遊戲'), '舰队Collection 是日本网络游戏')
        self.assertEqual(zm.trans_t2s('是消歧義頁面'), '是消歧义页面')
        self.assertEqual(zm.trans_t2s('陳公乾生'), '陈公乾生')

if __name__ == '__main__':
    php_conv.conv()
    unittest.main()
