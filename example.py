from zhhanz_conv import ZhhanzMan

zm = ZhhanzMan()
zm.trans_s2t('皇后在后面吃面')
# '皇后在後面吃麵'
zm.trans_t2s('皇后在後面吃麵')
# '皇后在后面吃面'