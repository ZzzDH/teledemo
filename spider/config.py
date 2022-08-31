questionlist = [{'id': "392726696", 'answer_count': "30"},
                {'id': "527445211", 'answer_count': "605"},
                {'id': "457368252", 'answer_count': "423"},
                {'id': "527153127", 'answer_count': "1707"}, ]

user_agent_list = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
]

questionurl1 = "https://www.zhihu.com/api/v4/questions/"
questionurl2 = "/similar-questions?include=data%5B*%5D.answer_count%2Cauthor%2Cfollower_count&limit=5"
answerurl1 = 'https://www.zhihu.com/api/v4/questions//'
answerurl2 = '/answers?include=data%5B%2A%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed' \
             '%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit' \
             '%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cattachment%2Cvoteup_count' \
             '%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info' \
             '%2Cquestion%2Cexcerpt%2Cis_labeled%2Cpaid_info%2Cpaid_info_content%2Crelationship.is_authorized' \
             '%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_recognized%3Bdata%5B%2A%5D.settings' \
             '.table_of_content.enabled&limit=5&offset=0' \
             '&platform=desktop&sort_by=default'

conditiondata = {'疫情': {'x-zse-96': '2.0_HDO4ma+TUPSDaU6THeY2TDQGyiqe2xc/obgnA7i8Y72quxDFN5li5yp8lj37=KY7',
                        'x-zst-81': '3_2.0VhnTj77m-qofgh3TxTnq2_Qq2LYuDhV80wSL77u0r6PxrXYqXRFZei90-LS9-hp1DufI'
                                    '-we8gGHPgJO1xuPZ0GxCTJHR7820XM20cLRGDJXfgGCBxupMuD_Ie8FL7AtqM6O1VDQyQ6nxrRPCHukMoCXBEgOsiRP0XL2ZUBXmDDV9qhnyTXFMnXcTF_ntRueThMOKTr3KuCtxfvHCNvHOpr9KtUYB2Tw1TuVqhcu18htVk0gmpGtBr7SLCCVPvRF1Xck0qrU92UNs-wYGM7FqicCBtqpMfg2L8iSmQL30LCg8yBO06hcMZBeYOhFMPwLCgBeV0vV8yDNs6Ce9fX2LQ0CLoUw8ZC2VfQOCfuVZeJx1LuFC4qfz2bOmoUHXS_X0iwc1cLSqS0H_j9O83ggByqH0AGos68FB1MXYEJrLYu2OWwXmJUwfBDUYIDpOOqO0RwCKFGLyoHSmbGcmBAe9rQLyaqpKUgY0-wXBwBHC'},
                 '新冠': {'x-zse-96': ' 2.0_jShyxkWiaJHHvXcsa+erlHQjHC/m+F/tBVBH+N25LdIPCFTAFF=5sB+TGcVH6WnG',
                        'x-zst-81': '3_2.0VhnTj77m-qofgh3TxTnq2_Qq2LYuDhV80wSL77u0r6PxrXYqXRFZei90-LS9-hp1DufI-we8gGHPgJO1xuPZ0GxCTJHR7820XM20cLRGDJXfgGCBxupMuD_Ie8FL7AtqM6O1VDQyQ6nxrRPCHukMoCXBEgOsiRP0XL2ZUBXmDDV9qhnyTXFMnXcTF_ntRueThLOC6wO0QhHVPhH9HGYOEJCK8hwpNBpClUX0pUOGyJHptD312wFM3rXfNGLPvRF1Xck0qrU92UNs-wYGM7FqicCBtqpMfg2L8iSmQL30LCg8yBO06hcMZBeYOhFMPwLCgBeV0vV8yDNs6Ce9fX2LQ0CLoUw8ZC2VfQOCfuVZeJx1LuFC4qfzeQXKPgOpk_LBpcn_2Q3fe0Op8g3fuU3M-uHmW9N8rCoMkCH9kqO_WUtYLGtm8TLqBcH_fB291Ug9p9SVrQpMcDX9jhHC5gg0yrrfYvx1yuwK-wXO-JrC'},
                 '疫苗': {'x-zse-96': '2.0_yDPoPWvjNkwc=lT/JqBgfbi7ngPjiwLvyk8gK6WWm7mS7j=XzP+agRs5dwGC2YFP',
                        'x-zst-81': '3_2.0VhnTj77m-qofgh3TxTnq2_Qq2LYuDhV80wSL77u0r6PxrXYqXRFZei90-LS9-hp1DufI-we8gGHPgJO1xuPZ0GxCTJHR7820XM20cLRGDJXfgGCBxupMuD_Ie8FL7AtqM6O1VDQyQ6nxrRPCHukMoCXBEgOsiRP0XL2ZUBXmDDV9qhnyTXFMnXcTF_ntRueThTHLZDrYZbxBZrHK09g82CxM1BC_kcOBkGY13qS8hJHMahYGzcOqo0LYOgVPv0VC3vHfncg0tUFV0q3YKRVmJDufPvc1iGLKDC3OsqcMUvgOzDLC7Go_hG7GJCpmaDx1BcNqsg98XqX96LtBfhp9_geG3wofjDxy8CCKSApMkR218uY05qfzoD9YIhHB6Uof3q3fe09qkBYmQ0XB0wLmzqX9QhgKjCoYjvOYODUfrLO9J4OGpLe1kUpGWC3KkHgBtbOqAquK2rXYHq2mZhxK2MOMVCof9qVM5wLL68HC'}
                 }
