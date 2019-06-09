# ZhConverter
+ 使用 [MediaWiki](https://www.mediawiki.org/wiki/Download) 上的 `ZHConversion.php` 完成的簡繁轉換

## Preparation
+ 前往 [MediaWiki](https://www.mediawiki.org/wiki/Download) 下載最新版的 `MediaWiki.tar.gz`
+ 解壓縮後尋找 `ZhConversion.php`
  + 當前版本放置於 `./language/data/` 下
+ 使用 `php_conv.py` 提取簡繁對應
  + 產生簡繁對應的 `.txt` & `.pkl` 共四個檔案

## Usage
+ Example
    ```python
    from zhhanz_conv import ZhhanzMan

    zm = ZhhanzMan()
    zm.trans_s2t('皇后在后面吃面')
    # '皇后在後面吃麵'
    zm.trans_t2s('皇后在後面吃麵')
    # '皇后在后面吃面'
    ```

## Reference
+ [繁簡轉換教學](https://tinyurl.com/y4nqcjlw)
+ [MediaWiki](https://www.mediawiki.org/wiki/Download)