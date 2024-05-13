import requests

api_key = "A0SWmWVSEvB6_pdlSBL01xHJR__TBJaiwBpaOcL4mi2ooCP8pfrHyk77XiFW_uu2-KKv0-fEB0_XE9U4yGDNO7LsFd6ehvJn59o4DwhAWBROdylGvs3O-9oZBzNCZnYx"
url = f"https://api.yelp.com/v3/businesses/search?location=Tacoma&sort_by=best_match&limit=20&api_key={api_key}"

response = requests.get(url)

print(response)

tacoma_data = {
    "businesses": [
        {
            "id": "yD8fH2xeUzURUM8qMGbzHw",
            "alias": "kimchi-box-tacoma",
            "name": "Kimchi Box",
            "image_url": "https://s3-media1.fl.yelpcdn.com/bphoto/OTRuYRsNGJi_pOY9RxoNoQ/o.jpg",
            "is_closed": False,
            "url": "https://www.yelp.com/biz/kimchi-box-tacoma?adjust_creative=ZKhGl9Asv55quGIOH6hVeA&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=ZKhGl9Asv55quGIOH6hVeA",
            "review_count": 39,
            "categories": [
                {
                    "alias": "korean",
                    "title": "Korean"
                }
            ],
            "rating": 4.7,
            "coordinates": {
                "latitude": 47.233496,
                "longitude": -122.503373
            },
            "transactions": [],
            "location": {
                "address1": "4916 Center St",
                "address2": None,
                "address3": "",
                "city": "Tacoma",
                "zip_code": "98409",
                "country": "US",
                "state": "WA",
                "display_address": [
                    "4916 Center St",
                    "Tacoma, WA 98409"
                ]
            },
            "phone": "+12533527183",
            "display_phone": "(253) 352-7183",
            "distance": 3807.4784078353955
        },
        {
            "id": "xZnlRzauK2oUSl4v2rHPDQ",
            "alias": "the-momo-king-tacoma",
            "name": "The Momo King",
            "image_url": "https://s3-media3.fl.yelpcdn.com/bphoto/a4nRwHuJU_7xrNZzAjCrIw/o.jpg",
            "is_closed": False,
            "url": "https://www.yelp.com/biz/the-momo-king-tacoma?adjust_creative=ZKhGl9Asv55quGIOH6hVeA&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=ZKhGl9Asv55quGIOH6hVeA",
            "review_count": 88,
            "categories": [
                {
                    "alias": "himalayan",
                    "title": "Himalayan/Nepalese"
                }
            ],
            "rating": 4.7,
            "coordinates": {
                "latitude": 47.21539843678073,
                "longitude": -122.4676184276202
            },
            "transactions": [
                "pickup",
                "delivery"
            ],
            "price": "$$",
            "location": {
                "address1": "4502 S Steele St",
                "address2": "",
                "address3": None,
                "city": "Tacoma",
                "zip_code": "98409",
                "country": "US",
                "state": "WA",
                "display_address": [
                    "4502 S Steele St",
                    "Tacoma, WA 98409"
                ]
            },
            "phone": "+12533013362",
            "display_phone": "(253) 301-3362",
            "distance": 3181.7419694245878
        },
        {
            "id": "HurE9y2vT6rvkJnMq3MUug",
            "alias": "balcon-express-tacoma-3",
            "name": "Balcon Express",
            "image_url": "https://s3-media2.fl.yelpcdn.com/bphoto/zaUJ0uG7dJzJUorPXvNxZg/o.jpg",
            "is_closed": False,
            "url": "https://www.yelp.com/biz/balcon-express-tacoma-3?adjust_creative=ZKhGl9Asv55quGIOH6hVeA&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=ZKhGl9Asv55quGIOH6hVeA",
            "review_count": 114,
            "categories": [
                {
                    "alias": "tacos",
                    "title": "Tacos"
                },
                {
                    "alias": "salvadoran",
                    "title": "Salvadoran"
                }
            ],
            "rating": 4.7,
            "coordinates": {
                "latitude": 47.25514,
                "longitude": -122.47646
            },
            "transactions": [
                "pickup",
                "delivery"
            ],
            "location": {
                "address1": "3102 6th Ave",
                "address2": None,
                "address3": "",
                "city": "Tacoma",
                "zip_code": "98406",
                "country": "US",
                "state": "WA",
                "display_address": [
                    "3102 6th Ave",
                    "Tacoma, WA 98406"
                ]
            },
            "phone": "+12532123054",
            "display_phone": "(253) 212-3054",
            "distance": 2131.7450023864462
        },
        {
            "id": "37Pd-RvjfhmzZNQ2nK1WRA",
            "alias": "the-palace-kebab-tacoma",
            "name": "The Palace Kebab",
            "image_url": "https://s3-media3.fl.yelpcdn.com/bphoto/J6aUDzqwMBz9AykHDgtafg/o.jpg",
            "is_closed": False,
            "url": "https://www.yelp.com/biz/the-palace-kebab-tacoma?adjust_creative=ZKhGl9Asv55quGIOH6hVeA&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=ZKhGl9Asv55quGIOH6hVeA",
            "review_count": 75,
            "categories": [
                {
                    "alias": "kebab",
                    "title": "Kebab"
                }
            ],
            "rating": 4.9,
            "coordinates": {
                "latitude": 47.23976113884944,
                "longitude": -122.42731237445938
            },
            "transactions": [
                "pickup",
                "delivery"
            ],
            "location": {
                "address1": "430 E 25th St",
                "address2": "Ste 22",
                "address3": "",
                "city": "Tacoma",
                "zip_code": "98421",
                "country": "US",
                "state": "WA",
                "display_address": [
                    "430 E 25th St",
                    "Ste 22",
                    "Tacoma, WA 98421"
                ]
            },
            "phone": "+12532720845",
            "display_phone": "(253) 272-0845",
            "distance": 2114.514177162514
        },
        {
            "id": "R2lQIz3K68WM93jzT_siZw",
            "alias": "ooh-lala-burgers-tacoma",
            "name": "Ooh Lala Burgers",
            "image_url": "https://s3-media2.fl.yelpcdn.com/bphoto/ypLn5_3EkrTA6xG53Drxyw/o.jpg",
            "is_closed": False,
            "url": "https://www.yelp.com/biz/ooh-lala-burgers-tacoma?adjust_creative=ZKhGl9Asv55quGIOH6hVeA&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=ZKhGl9Asv55quGIOH6hVeA",
            "review_count": 295,
            "categories": [
                {
                    "alias": "burgers",
                    "title": "Burgers"
                },
                {
                    "alias": "foodstands",
                    "title": "Food Stands"
                }
            ],
            "rating": 4.8,
            "coordinates": {
                "latitude": 47.2673615860055,
                "longitude": -122.468008878186
            },
            "transactions": [
                "pickup",
                "delivery"
            ],
            "price": "$$",
            "location": {
                "address1": "1312 N I St",
                "address2": "",
                "address3": None,
                "city": "Tacoma",
                "zip_code": "98403",
                "country": "US",
                "state": "WA",
                "display_address": [
                    "1312 N I St",
                    "Tacoma, WA 98403"
                ]
            },
            "phone": "+14256983645",
            "display_phone": "(425) 698-3645",
            "distance": 2913.4018315864205
        },
        {
            "id": "6x2abkjR8U5eEZXDNQnMdA",
            "alias": "iron-pot-kent",
            "name": "Iron Pot",
            "image_url": "https://s3-media2.fl.yelpcdn.com/bphoto/WPrCyHE86Ug0eLPKh2vznw/o.jpg",
            "is_closed": False,
            "url": "https://www.yelp.com/biz/iron-pot-kent?adjust_creative=ZKhGl9Asv55quGIOH6hVeA&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=ZKhGl9Asv55quGIOH6hVeA",
            "review_count": 184,
            "categories": [
                {
                    "alias": "korean",
                    "title": "Korean"
                }
            ],
            "rating": 4.8,
            "coordinates": {
                "latitude": 47.380297,
                "longitude": -122.23329
            },
            "transactions": [
                "delivery"
            ],
            "price": "$$",
            "location": {
                "address1": "222 1st Ave S",
                "address2": "",
                "address3": None,
                "city": "Kent",
                "zip_code": "98032",
                "country": "US",
                "state": "WA",
                "display_address": [
                    "222 1st Ave S",
                    "Kent, WA 98032"
                ]
            },
            "phone": "+12532774905",
            "display_phone": "(253) 277-4905",
            "distance": 22659.651758506294
        },
        {
            "id": "OL2RHr5cqeFcezYpI4rQGA",
            "alias": "ericks-seafood-and-more-tacoma",
            "name": "Erick's Seafood and More",
            "image_url": "https://s3-media1.fl.yelpcdn.com/bphoto/Rni6ShXyJqFYcfdm6kw5dw/o.jpg",
            "is_closed": False,
            "url": "https://www.yelp.com/biz/ericks-seafood-and-more-tacoma?adjust_creative=ZKhGl9Asv55quGIOH6hVeA&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=ZKhGl9Asv55quGIOH6hVeA",
            "review_count": 26,
            "categories": [
                {
                    "alias": "streetvendors",
                    "title": "Street Vendors"
                },
                {
                    "alias": "foodtrucks",
                    "title": "Food Trucks"
                },
                {
                    "alias": "seafood",
                    "title": "Seafood"
                }
            ],
            "rating": 4.7,
            "coordinates": {
                "latitude": 47.2550043,
                "longitude": -122.4957086
            },
            "transactions": [],
            "price": "$$",
            "location": {
                "address1": "4328 6th Ave",
                "address2": "",
                "address3": None,
                "city": "Tacoma ",
                "zip_code": "98406",
                "country": "US",
                "state": "WA",
                "display_address": [
                    "4328 6th Ave",
                    "Tacoma , WA 98406"
                ]
            },
            "phone": "+13605628311",
            "display_phone": "(360) 562-8311",
            "distance": 3364.6334562781794
        },
        {
            "id": "bUBiBh6HRV--sbX5DAYYUg",
            "alias": "jin-jin-matcha-tacoma",
            "name": "Jin Jin Matcha",
            "image_url": "https://s3-media2.fl.yelpcdn.com/bphoto/OT0dbPQOcTdGrnLKErhG6w/o.jpg",
            "is_closed": False,
            "url": "https://www.yelp.com/biz/jin-jin-matcha-tacoma?adjust_creative=ZKhGl9Asv55quGIOH6hVeA&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=ZKhGl9Asv55quGIOH6hVeA",
            "review_count": 49,
            "categories": [
                {
                    "alias": "tea",
                    "title": "Tea Rooms"
                }
            ],
            "rating": 4.8,
            "coordinates": {
                "latitude": 47.25358207824086,
                "longitude": -122.4383984723903
            },
            "transactions": [],
            "location": {
                "address1": "1019 Pacific Ave",
                "address2": "",
                "address3": None,
                "city": "Tacoma",
                "zip_code": "98402",
                "country": "US",
                "state": "WA",
                "display_address": [
                    "1019 Pacific Ave",
                    "Tacoma, WA 98402"
                ]
            },
            "phone": "",
            "display_phone": "",
            "distance": 1741.5082731945088
        },
        {
            "id": "usAVRmfiO7kMLOiJ40KKYg",
            "alias": "moobongri-soondae-federal-way-federal-way",
            "name": "Moobongri Soondae Federal Way",
            "image_url": "https://s3-media4.fl.yelpcdn.com/bphoto/HTZCI7UHIDWu2JOJPt1ORQ/o.jpg",
            "is_closed": False,
            "url": "https://www.yelp.com/biz/moobongri-soondae-federal-way-federal-way?adjust_creative=ZKhGl9Asv55quGIOH6hVeA&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=ZKhGl9Asv55quGIOH6hVeA",
            "review_count": 14,
            "categories": [
                {
                    "alias": "korean",
                    "title": "Korean"
                }
            ],
            "rating": 4.6,
            "coordinates": {
                "latitude": 47.30271550199792,
                "longitude": -122.3129211591431
            },
            "transactions": [],
            "location": {
                "address1": "33320 Pacific Hwy S",
                "address2": "Ste 101",
                "address3": "",
                "city": "Federal Way",
                "zip_code": "98003",
                "country": "US",
                "state": "WA",
                "display_address": [
                    "33320 Pacific Hwy S",
                    "Ste 101",
                    "Federal Way, WA 98003"
                ]
            },
            "phone": "+12535179233",
            "display_phone": "(253) 517-9233",
            "distance": 12626.281566321493
        },
        {
            "id": "SvpZFYnWANObpJW6MTEZig",
            "alias": "buddy-s-chicken-and-waffles-tacoma",
            "name": "Buddy’s Chicken & Waffles",
            "image_url": "https://s3-media2.fl.yelpcdn.com/bphoto/uaF4--RPzLjiQkDzpxw7pw/o.jpg",
            "is_closed": False,
            "url": "https://www.yelp.com/biz/buddy-s-chicken-and-waffles-tacoma?adjust_creative=ZKhGl9Asv55quGIOH6hVeA&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=ZKhGl9Asv55quGIOH6hVeA",
            "review_count": 163,
            "categories": [
                {
                    "alias": "waffles",
                    "title": "Waffles"
                },
                {
                    "alias": "chickenshop",
                    "title": "Chicken Shop"
                },
                {
                    "alias": "sandwiches",
                    "title": "Sandwiches"
                }
            ],
            "rating": 4.8,
            "coordinates": {
                "latitude": 47.22423519645566,
                "longitude": -122.44029783624256
            },
            "transactions": [],
            "location": {
                "address1": "3709 S G St",
                "address2": None,
                "address3": "",
                "city": "Tacoma",
                "zip_code": "98418",
                "country": "US",
                "state": "WA",
                "display_address": [
                    "3709 S G St",
                    "Tacoma, WA 98418"
                ]
            },
            "phone": "+12532011550",
            "display_phone": "(253) 201-1550",
            "distance": 2333.235508665499
        },
        {
            "id": "b7nMKW2k_u1oPM30ce1peQ",
            "alias": "noodle-house-kent-4",
            "name": "Noodle House",
            "image_url": "https://s3-media1.fl.yelpcdn.com/bphoto/bKcKQUdd8Q9_KC_FFu6Q3A/o.jpg",
            "is_closed": False,
            "url": "https://www.yelp.com/biz/noodle-house-kent-4?adjust_creative=ZKhGl9Asv55quGIOH6hVeA&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=ZKhGl9Asv55quGIOH6hVeA",
            "review_count": 105,
            "categories": [
                {
                    "alias": "noodles",
                    "title": "Noodles"
                },
                {
                    "alias": "chinese",
                    "title": "Chinese"
                },
                {
                    "alias": "soup",
                    "title": "Soup"
                }
            ],
            "rating": 4.5,
            "coordinates": {
                "latitude": 47.439425164161186,
                "longitude": -122.22079133189402
            },
            "transactions": [],
            "location": {
                "address1": "18126 E Valley Hwy",
                "address2": "",
                "address3": None,
                "city": "Kent",
                "zip_code": "98032",
                "country": "US",
                "state": "WA",
                "display_address": [
                    "18126 E Valley Hwy",
                    "Kent, WA 98032"
                ]
            },
            "phone": "+12539813399",
            "display_phone": "(253) 981-3399",
            "distance": 28105.503914064317
        },
        {
            "id": "RfBkkXicWuTTeBQMyFBfCQ",
            "alias": "ebadom-federal-way",
            "name": "Ebadom",
            "image_url": "https://s3-media1.fl.yelpcdn.com/bphoto/AwEJgve2khqLKL4PLHaMLw/o.jpg",
            "is_closed": False,
            "url": "https://www.yelp.com/biz/ebadom-federal-way?adjust_creative=ZKhGl9Asv55quGIOH6hVeA&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=ZKhGl9Asv55quGIOH6hVeA",
            "review_count": 27,
            "categories": [
                {
                    "alias": "korean",
                    "title": "Korean"
                }
            ],
            "rating": 4.4,
            "coordinates": {
                "latitude": 47.30274971254008,
                "longitude": -122.31222088700488
            },
            "transactions": [],
            "location": {
                "address1": "33304 Pacific Hwy S",
                "address2": "Ste 307",
                "address3": None,
                "city": "Federal Way",
                "zip_code": "98003",
                "country": "US",
                "state": "WA",
                "display_address": [
                    "33304 Pacific Hwy S",
                    "Ste 307",
                    "Federal Way, WA 98003"
                ]
            },
            "phone": "",
            "display_phone": "",
            "distance": 12673.163131523019
        },
        {
            "id": "Q9RusjzOKGm-JGPiwOV2Mg",
            "alias": "s-level-tea-tacoma",
            "name": "S Level Tea",
            "image_url": "https://s3-media1.fl.yelpcdn.com/bphoto/Kdq4n02j42i-yxWk9mjG3w/o.jpg",
            "is_closed": False,
            "url": "https://www.yelp.com/biz/s-level-tea-tacoma?adjust_creative=ZKhGl9Asv55quGIOH6hVeA&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=ZKhGl9Asv55quGIOH6hVeA",
            "review_count": 0,
            "categories": [
                {
                    "alias": "bubbletea",
                    "title": "Bubble Tea"
                }
            ],
            "rating": 0,
            "coordinates": {
                "latitude": 47.24618,
                "longitude": -122.43733
            },
            "transactions": [],
            "location": {
                "address1": "1724 Pacific Ave",
                "address2": None,
                "address3": "",
                "city": "Tacoma",
                "zip_code": "98402",
                "country": "US",
                "state": "WA",
                "display_address": [
                    "1724 Pacific Ave",
                    "Tacoma, WA 98402"
                ]
            },
            "phone": "+12536272111",
            "display_phone": "(253) 627-2111",
            "distance": 1395.4954938289366
        },
        {
            "id": "2DAbRNuyxM_cd1p0D82bcQ",
            "alias": "happy-belly-tacoma",
            "name": "Happy Belly",
            "image_url": "https://s3-media3.fl.yelpcdn.com/bphoto/W3FCy1KgRdB_OAUIWcHFoA/o.jpg",
            "is_closed": False,
            "url": "https://www.yelp.com/biz/happy-belly-tacoma?adjust_creative=ZKhGl9Asv55quGIOH6hVeA&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=ZKhGl9Asv55quGIOH6hVeA",
            "review_count": 148,
            "categories": [
                {
                    "alias": "juicebars",
                    "title": "Juice Bars & Smoothies"
                },
                {
                    "alias": "wraps",
                    "title": "Wraps"
                },
                {
                    "alias": "sandwiches",
                    "title": "Sandwiches"
                }
            ],
            "rating": 4.5,
            "coordinates": {
                "latitude": 47.252269744873,
                "longitude": -122.441757202148
            },
            "transactions": [
                "pickup",
                "delivery"
            ],
            "price": "$$",
            "location": {
                "address1": "1122 Market St",
                "address2": None,
                "address3": "",
                "city": "Tacoma",
                "zip_code": "98402",
                "country": "US",
                "state": "WA",
                "display_address": [
                    "1122 Market St",
                    "Tacoma, WA 98402"
                ]
            },
            "phone": "+12533656706",
            "display_phone": "(253) 365-6706",
            "distance": 1460.7034492386065
        },
        {
            "id": "MdNGMrvmjgVWvu2w5u7XPw",
            "alias": "lucky-penny-cafe-and-deli-tacoma",
            "name": "Lucky Penny Cafe & Deli",
            "image_url": "https://s3-media2.fl.yelpcdn.com/bphoto/R-7n-mOdFAT_lVVn4uzO1Q/o.jpg",
            "is_closed": False,
            "url": "https://www.yelp.com/biz/lucky-penny-cafe-and-deli-tacoma?adjust_creative=ZKhGl9Asv55quGIOH6hVeA&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=ZKhGl9Asv55quGIOH6hVeA",
            "review_count": 46,
            "categories": [
                {
                    "alias": "cafes",
                    "title": "Cafes"
                },
                {
                    "alias": "delis",
                    "title": "Delis"
                }
            ],
            "rating": 4.7,
            "coordinates": {
                "latitude": 47.253567,
                "longitude": -122.439079
            },
            "transactions": [
                "delivery"
            ],
            "price": "$",
            "location": {
                "address1": "950 Pacific Ave",
                "address2": "",
                "address3": "",
                "city": "Tacoma",
                "zip_code": "98402",
                "country": "US",
                "state": "WA",
                "display_address": [
                    "950 Pacific Ave",
                    "Tacoma, WA 98402"
                ]
            },
            "phone": "+12533833814",
            "display_phone": "(253) 383-3814",
            "distance": 1701.0810109821134
        },
        {
            "id": "KGOncoGpvrzGI4kDC1oXSw",
            "alias": "manuscript-and-dialogue-tacoma",
            "name": "Manuscript & Dialogue",
            "image_url": "https://s3-media3.fl.yelpcdn.com/bphoto/ekGJdHqU1C4E_2-nPZmknA/o.jpg",
            "is_closed": False,
            "url": "https://www.yelp.com/biz/manuscript-and-dialogue-tacoma?adjust_creative=ZKhGl9Asv55quGIOH6hVeA&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=ZKhGl9Asv55quGIOH6hVeA",
            "review_count": 17,
            "categories": [
                {
                    "alias": "cocktailbars",
                    "title": "Cocktail Bars"
                },
                {
                    "alias": "danceclubs",
                    "title": "Dance Clubs"
                },
                {
                    "alias": "newamerican",
                    "title": "New American"
                }
            ],
            "rating": 4.3,
            "coordinates": {
                "latitude": 47.2619,
                "longitude": -122.44611
            },
            "transactions": [
                "pickup",
                "delivery"
            ],
            "location": {
                "address1": "203 Tacoma Ave S",
                "address2": "",
                "address3": None,
                "city": "Tacoma",
                "zip_code": "98402",
                "country": "US",
                "state": "WA",
                "display_address": [
                    "203 Tacoma Ave S",
                    "Tacoma, WA 98402"
                ]
            },
            "phone": "+12532120779",
            "display_phone": "(253) 212-0779",
            "distance": 2235.0238978528755
        },
        {
            "id": "0DqclI2TQIOxnHEUm_2NZg",
            "alias": "tacoma-shawarma-tacoma",
            "name": "Tacoma Shawarma",
            "image_url": "https://s3-media1.fl.yelpcdn.com/bphoto/HXWzbYsrBLrHfLybKUBRTw/o.jpg",
            "is_closed": False,
            "url": "https://www.yelp.com/biz/tacoma-shawarma-tacoma?adjust_creative=ZKhGl9Asv55quGIOH6hVeA&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=ZKhGl9Asv55quGIOH6hVeA",
            "review_count": 8,
            "categories": [
                {
                    "alias": "kebab",
                    "title": "Kebab"
                },
                {
                    "alias": "hotdogs",
                    "title": "Fast Food"
                }
            ],
            "rating": 4.8,
            "coordinates": {
                "latitude": 47.21432678812206,
                "longitude": -122.473266808258
            },
            "transactions": [],
            "location": {
                "address1": "4704 S Oakes St",
                "address2": "Ste 6400",
                "address3": None,
                "city": "Tacoma",
                "zip_code": "98409",
                "country": "US",
                "state": "WA",
                "display_address": [
                    "4704 S Oakes St",
                    "Ste 6400",
                    "Tacoma, WA 98409"
                ]
            },
            "phone": "+12538788966",
            "display_phone": "(253) 878-8966",
            "distance": 3443.3483978609906
        },
        {
            "id": "jLAnkmyrAzhNsQ-NdTw9Ag",
            "alias": "one-day-cafe-lakewood",
            "name": "One Day Cafe",
            "image_url": "https://s3-media3.fl.yelpcdn.com/bphoto/9S9Yav_KNXgnwvU9hQE22Q/o.jpg",
            "is_closed": False,
            "url": "https://www.yelp.com/biz/one-day-cafe-lakewood?adjust_creative=ZKhGl9Asv55quGIOH6hVeA&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=ZKhGl9Asv55quGIOH6hVeA",
            "review_count": 67,
            "categories": [
                {
                    "alias": "coffee",
                    "title": "Coffee & Tea"
                },
                {
                    "alias": "bubbletea",
                    "title": "Bubble Tea"
                },
                {
                    "alias": "desserts",
                    "title": "Desserts"
                }
            ],
            "rating": 4.8,
            "coordinates": {
                "latitude": 47.169757,
                "longitude": -122.483191
            },
            "transactions": [],
            "price": "$$",
            "location": {
                "address1": "9601 S Tacoma Way",
                "address2": "Ste 101",
                "address3": "",
                "city": "Lakewood",
                "zip_code": "98499",
                "country": "US",
                "state": "WA",
                "display_address": [
                    "9601 S Tacoma Way",
                    "Ste 101",
                    "Lakewood, WA 98499"
                ]
            },
            "phone": "+12539488967",
            "display_phone": "(253) 948-8967",
            "distance": 8383.32923994902
        },
        {
            "id": "4Wb7Hj_iZjDq_04-He3ssw",
            "alias": "toast-mi-tacoma",
            "name": "Toast Mi",
            "image_url": "https://s3-media3.fl.yelpcdn.com/bphoto/rc3QtSRjzvfXochDYbgUAw/o.jpg",
            "is_closed": False,
            "url": "https://www.yelp.com/biz/toast-mi-tacoma?adjust_creative=ZKhGl9Asv55quGIOH6hVeA&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=ZKhGl9Asv55quGIOH6hVeA",
            "review_count": 187,
            "categories": [
                {
                    "alias": "vietnamese",
                    "title": "Vietnamese"
                }
            ],
            "rating": 4.5,
            "coordinates": {
                "latitude": 47.27131,
                "longitude": -122.48915
            },
            "transactions": [
                "pickup",
                "delivery"
            ],
            "price": "$",
            "location": {
                "address1": "2602 N Proctor St",
                "address2": "Ste D",
                "address3": None,
                "city": "Tacoma",
                "zip_code": "98407",
                "country": "US",
                "state": "WA",
                "display_address": [
                    "2602 N Proctor St",
                    "Ste D",
                    "Tacoma, WA 98407"
                ]
            },
            "phone": "+12532452246",
            "display_phone": "(253) 245-2246",
            "distance": 4095.0084658911724
        },
        {
            "id": "nP7wr9Ns4TnAub5GM-anGA",
            "alias": "yaki-raki-tacoma",
            "name": "Yaki Raki",
            "image_url": "https://s3-media4.fl.yelpcdn.com/bphoto/btLyZ4iSYk-C_J0sILX9WA/o.jpg",
            "is_closed": False,
            "url": "https://www.yelp.com/biz/yaki-raki-tacoma?adjust_creative=ZKhGl9Asv55quGIOH6hVeA&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=ZKhGl9Asv55quGIOH6hVeA",
            "review_count": 34,
            "categories": [
                {
                    "alias": "sushi",
                    "title": "Sushi Bars"
                },
                {
                    "alias": "ramen",
                    "title": "Ramen"
                }
            ],
            "rating": 4.5,
            "coordinates": {
                "latitude": 47.23643897911414,
                "longitude": -122.47792531628306
            },
            "transactions": [
                "pickup",
                "delivery"
            ],
            "price": "$$",
            "location": {
                "address1": "3202 S 23rd St",
                "address2": "Ste F7",
                "address3": "",
                "city": "Tacoma",
                "zip_code": "98405",
                "country": "US",
                "state": "WA",
                "display_address": [
                    "3202 S 23rd St",
                    "Ste F7",
                    "Tacoma, WA 98405"
                ]
            },
            "phone": "+12532121223",
            "display_phone": "(253) 212-1223",
            "distance": 1866.2974227395566
        }
    ],
    "total": 7100,
    "region": {
        "center": {
            "longitude": -122.45498657226562,
            "latitude": 47.24269656302497
        }
    }
}
tacoma_restaurants = tacoma_data['businesses']
tacoma_ids = []
tacoma_names = []
for restaurant in tacoma_restaurants:
    tacoma_ids.append(restaurant['id'])
    tacoma_names.append(restaurant['name'])

la_data = {
  "businesses": [
    {
      "id": "64BprBYS6h9yliVX_rXlxg",
      "alias": "joyce-los-angeles-2",
      "name": "Joyce",
      "image_url": "https://s3-media2.fl.yelpcdn.com/bphoto/vbe6ANgDe_n14fhiXj6YqA/o.jpg",
      "is_closed": False,
      "url": "https://www.yelp.com/biz/joyce-los-angeles-2?adjust_creative=ZKhGl9Asv55quGIOH6hVeA&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=ZKhGl9Asv55quGIOH6hVeA",
      "review_count": 284,
      "categories": [
        {
          "alias": "southern",
          "title": "Southern"
        },
        {
          "alias": "newamerican",
          "title": "New American"
        },
        {
          "alias": "seafood",
          "title": "Seafood"
        }
      ],
      "rating": 4.4,
      "coordinates": {
        "latitude": 34.04645515952082,
        "longitude": -118.2571682
      },
      "transactions": [],
      "location": {
        "address1": "770 S Grand Ave",
        "address2": "Ste A",
        "address3": "",
        "city": "Los Angeles",
        "zip_code": "90017",
        "country": "US",
        "state": "CA",
        "display_address": [
          "770 S Grand Ave",
          "Ste A",
          "Los Angeles, CA 90017"
        ]
      },
      "phone": "+12133950202",
      "display_phone": "(213) 395-0202",
      "distance": 6150.345321434559
    },
    {
      "id": "kgA43j16Mh-UEAEP8Y_tTw",
      "alias": "rice-chicken-los-angeles-2",
      "name": "Rice Chicken",
      "image_url": "https://s3-media4.fl.yelpcdn.com/bphoto/lJ5xHfuq-Vh1m-2dH6FgKQ/o.jpg",
      "is_closed": False,
      "url": "https://www.yelp.com/biz/rice-chicken-los-angeles-2?adjust_creative=ZKhGl9Asv55quGIOH6hVeA&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=ZKhGl9Asv55quGIOH6hVeA",
      "review_count": 111,
      "categories": [
        {
          "alias": "chickenshop",
          "title": "Chicken Shop"
        }
      ],
      "rating": 4.8,
      "coordinates": {
        "latitude": 34.0580878,
        "longitude": -118.2937735
      },
      "transactions": [],
      "price": "$$",
      "location": {
        "address1": "3065 W 8th St",
        "address2": None,
        "address3": "",
        "city": "Los Angeles",
        "zip_code": "90005",
        "country": "US",
        "state": "CA",
        "display_address": [
          "3065 W 8th St",
          "Los Angeles, CA 90005"
        ]
      },
      "phone": "+12139086996",
      "display_phone": "(213) 908-6996",
      "distance": 2584.920800330865
    },
    {
      "id": "8lzAX-Uc4o7dwaXnulAFIQ",
      "alias": "lius-cafe-los-angeles",
      "name": "Liu's Cafe",
      "image_url": "https://s3-media2.fl.yelpcdn.com/bphoto/2aNMFzwkNvySrI3rqHxy2w/o.jpg",
      "is_closed": False,
      "url": "https://www.yelp.com/biz/lius-cafe-los-angeles?adjust_creative=ZKhGl9Asv55quGIOH6hVeA&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=ZKhGl9Asv55quGIOH6hVeA",
      "review_count": 221,
      "categories": [
        {
          "alias": "cafes",
          "title": "Cafes"
        },
        {
          "alias": "chinese",
          "title": "Chinese"
        },
        {
          "alias": "taiwanese",
          "title": "Taiwanese"
        }
      ],
      "rating": 4.4,
      "coordinates": {
        "latitude": 34.06365,
        "longitude": -118.30844
      },
      "transactions": [],
      "price": "$$",
      "location": {
        "address1": "3915 1/2 W 6th St",
        "address2": None,
        "address3": "",
        "city": "Los Angeles",
        "zip_code": "90020",
        "country": "US",
        "state": "CA",
        "display_address": [
          "3915 1/2 W 6th St",
          "Los Angeles, CA 90020"
        ]
      },
      "phone": "+12135683686",
      "display_phone": "(213) 568-3686",
      "distance": 1214.1039472538732
    },
    {
      "id": "KbxnCK_rbDgGSAvH1fCjeQ",
      "alias": "cafe-bandal-los-angeles",
      "name": "Cafe Bandal",
      "image_url": "https://s3-media4.fl.yelpcdn.com/bphoto/w6_4tMCVN94egmjWzMOvew/o.jpg",
      "is_closed": False,
      "url": "https://www.yelp.com/biz/cafe-bandal-los-angeles?adjust_creative=ZKhGl9Asv55quGIOH6hVeA&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=ZKhGl9Asv55quGIOH6hVeA",
      "review_count": 8,
      "categories": [
        {
          "alias": "desserts",
          "title": "Desserts"
        },
        {
          "alias": "cafes",
          "title": "Cafes"
        }
      ],
      "rating": 5,
      "coordinates": {
        "latitude": 34.05879,
        "longitude": -118.308646
      },
      "transactions": [],
      "location": {
        "address1": "730 S Western Ave",
        "address2": "Ste 104",
        "address3": "",
        "city": "Los Angeles",
        "zip_code": "90005",
        "country": "US",
        "state": "CA",
        "display_address": [
          "730 S Western Ave",
          "Ste 104",
          "Los Angeles, CA 90005"
        ]
      },
      "phone": "+13238806856",
      "display_phone": "(323) 880-6856",
      "distance": 1215.9705878383338
    },
    {
      "id": "eFSyURx8qNHWpXoV_zCLbg",
      "alias": "flour-fresh-cream-donut-los-angeles",
      "name": "Flour Fresh Cream Donut",
      "image_url": "https://s3-media4.fl.yelpcdn.com/bphoto/m8Zur-_CQgh_VCyRIroqew/o.jpg",
      "is_closed": False,
      "url": "https://www.yelp.com/biz/flour-fresh-cream-donut-los-angeles?adjust_creative=ZKhGl9Asv55quGIOH6hVeA&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=ZKhGl9Asv55quGIOH6hVeA",
      "review_count": 91,
      "categories": [
        {
          "alias": "donuts",
          "title": "Donuts"
        },
        {
          "alias": "desserts",
          "title": "Desserts"
        },
        {
          "alias": "sandwiches",
          "title": "Sandwiches"
        }
      ],
      "rating": 4.8,
      "coordinates": {
        "latitude": 34.057289738210116,
        "longitude": -118.3092634890533
      },
      "transactions": [],
      "location": {
        "address1": "833 S Western Ave",
        "address2": "Ste 38",
        "address3": None,
        "city": "Los Angeles",
        "zip_code": "90005",
        "country": "US",
        "state": "CA",
        "display_address": [
          "833 S Western Ave",
          "Ste 38",
          "Los Angeles, CA 90005"
        ]
      },
      "phone": "+12135079292",
      "display_phone": "(213) 507-9292",
      "distance": 1214.317392853436
    },
    {
      "id": "-dmFlY8oohLiep_sexSMSg",
      "alias": "tita-lina-s-los-angeles",
      "name": "Tita Lina’s",
      "image_url": "https://s3-media2.fl.yelpcdn.com/bphoto/pcXRqx9bEPVTpCFbxcBTjg/o.jpg",
      "is_closed": False,
      "url": "https://www.yelp.com/biz/tita-lina-s-los-angeles?adjust_creative=ZKhGl9Asv55quGIOH6hVeA&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=ZKhGl9Asv55quGIOH6hVeA",
      "review_count": 70,
      "categories": [
        {
          "alias": "filipino",
          "title": "Filipino"
        }
      ],
      "rating": 4.9,
      "coordinates": {
        "latitude": 34.07223538659772,
        "longitude": -118.274630116813
      },
      "transactions": [],
      "price": "$$",
      "location": {
        "address1": "2532 W Temple St",
        "address2": "",
        "address3": None,
        "city": "Los Angeles",
        "zip_code": "90026",
        "country": "US",
        "state": "CA",
        "display_address": [
          "2532 W Temple St",
          "Los Angeles, CA 90026"
        ]
      },
      "phone": "+12136747572",
      "display_phone": "(213) 674-7572",
      "distance": 4466.022084069886
    },
    {
      "id": "BEJU1_EDtayPPmDXlUIknw",
      "alias": "sonoratown-los-angeles-2",
      "name": "Sonoratown",
      "image_url": "https://s3-media3.fl.yelpcdn.com/bphoto/sJn18Dn_ukXWsMJv1uDvXg/o.jpg",
      "is_closed": False,
      "url": "https://www.yelp.com/biz/sonoratown-los-angeles-2?adjust_creative=ZKhGl9Asv55quGIOH6hVeA&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=ZKhGl9Asv55quGIOH6hVeA",
      "review_count": 231,
      "categories": [
        {
          "alias": "mexican",
          "title": "Mexican"
        }
      ],
      "rating": 4.5,
      "coordinates": {
        "latitude": 34.05396,
        "longitude": -118.35523
      },
      "transactions": [],
      "location": {
        "address1": "5610 San Vicente Blvd",
        "address2": None,
        "address3": "",
        "city": "Los Angeles",
        "zip_code": "90019",
        "country": "US",
        "state": "CA",
        "display_address": [
          "5610 San Vicente Blvd",
          "Los Angeles, CA 90019"
        ]
      },
      "phone": "+12132225071",
      "display_phone": "(213) 222-5071",
      "distance": 3239.1417830516134
    },
    {
      "id": "vR2LjJP3beB56AuPGSBSJw",
      "alias": "kazunori-mid-wilshire-los-angeles",
      "name": "KazuNori | Mid-Wilshire",
      "image_url": "https://s3-media4.fl.yelpcdn.com/bphoto/FSYVq9dvmaswW53FOR4RXQ/o.jpg",
      "is_closed": False,
      "url": "https://www.yelp.com/biz/kazunori-mid-wilshire-los-angeles?adjust_creative=ZKhGl9Asv55quGIOH6hVeA&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=ZKhGl9Asv55quGIOH6hVeA",
      "review_count": 335,
      "categories": [
        {
          "alias": "sushi",
          "title": "Sushi Bars"
        },
        {
          "alias": "japanese",
          "title": "Japanese"
        }
      ],
      "rating": 4.3,
      "coordinates": {
        "latitude": 34.06372,
        "longitude": -118.36446
      },
      "transactions": [],
      "price": "$$",
      "location": {
        "address1": "6245 Wilshire Blvd",
        "address2": "Ste 101",
        "address3": None,
        "city": "Los Angeles",
        "zip_code": "90048",
        "country": "US",
        "state": "CA",
        "display_address": [
          "6245 Wilshire Blvd",
          "Ste 101",
          "Los Angeles, CA 90048"
        ]
      },
      "phone": "+13236426457",
      "display_phone": "(323) 642-6457",
      "distance": 4012.8966457689808
    },
    {
      "id": "beA_DlDpij8O9xK2B-NjEA",
      "alias": "mex-peru-gipsy-los-angeles-9",
      "name": "Mex Peru Gipsy",
      "image_url": "https://s3-media2.fl.yelpcdn.com/bphoto/N2j7_-YFQLxdl6PpfaA_dA/o.jpg",
      "is_closed": False,
      "url": "https://www.yelp.com/biz/mex-peru-gipsy-los-angeles-9?adjust_creative=ZKhGl9Asv55quGIOH6hVeA&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=ZKhGl9Asv55quGIOH6hVeA",
      "review_count": 1754,
      "categories": [
        {
          "alias": "mexican",
          "title": "Mexican"
        },
        {
          "alias": "peruvian",
          "title": "Peruvian"
        },
        {
          "alias": "seafood",
          "title": "Seafood"
        }
      ],
      "rating": 4.8,
      "coordinates": {
        "latitude": 34.03518711471021,
        "longitude": -118.25592540194448
      },
      "transactions": [
        "delivery",
        "pickup"
      ],
      "price": "$$",
      "location": {
        "address1": "414 E 12th St",
        "address2": "",
        "address3": "",
        "city": "Los Angeles",
        "zip_code": "90015",
        "country": "US",
        "state": "CA",
        "display_address": [
          "414 E 12th St",
          "Los Angeles, CA 90015"
        ]
      },
      "phone": "+12137481773",
      "display_phone": "(213) 748-1773",
      "distance": 6707.179808666784
    },
    {
      "id": "mU2KjMSL73Z3kOUnfrK_dg",
      "alias": "for-the-win-los-angeles-4",
      "name": "For The Win",
      "image_url": "https://s3-media4.fl.yelpcdn.com/bphoto/gDyLMlG8l65B7Z9dxqUy_Q/o.jpg",
      "is_closed": False,
      "url": "https://www.yelp.com/biz/for-the-win-los-angeles-4?adjust_creative=ZKhGl9Asv55quGIOH6hVeA&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=ZKhGl9Asv55quGIOH6hVeA",
      "review_count": 138,
      "categories": [
        {
          "alias": "burgers",
          "title": "Burgers"
        },
        {
          "alias": "chickenshop",
          "title": "Chicken Shop"
        },
        {
          "alias": "sandwiches",
          "title": "Sandwiches"
        }
      ],
      "rating": 3.9,
      "coordinates": {
        "latitude": 34.050782,
        "longitude": -118.248775
      },
      "transactions": [],
      "price": "$$",
      "location": {
        "address1": "317 S Broadway",
        "address2": "",
        "address3": None,
        "city": "Los Angeles",
        "zip_code": "90013",
        "country": "US",
        "state": "CA",
        "display_address": [
          "317 S Broadway",
          "Los Angeles, CA 90013"
        ]
      },
      "phone": "",
      "display_phone": "",
      "distance": 6740.418682821416
    },
    {
      "id": "BqnCPLovloQPLzY7-t-oNg",
      "alias": "thai-night-market-los-angeles",
      "name": "Thai Night Market",
      "image_url": "https://s3-media4.fl.yelpcdn.com/bphoto/UbgErZz9bwgcKYbaVKj5Vw/o.jpg",
      "is_closed": False,
      "url": "https://www.yelp.com/biz/thai-night-market-los-angeles?adjust_creative=ZKhGl9Asv55quGIOH6hVeA&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=ZKhGl9Asv55quGIOH6hVeA",
      "review_count": 31,
      "categories": [
        {
          "alias": "streetvendors",
          "title": "Street Vendors"
        }
      ],
      "rating": 4.5,
      "coordinates": {
        "latitude": 34.09770197296509,
        "longitude": -118.3050083
      },
      "transactions": [],
      "location": {
        "address1": "5270 Sunset Blvd",
        "address2": "",
        "address3": None,
        "city": "Los Angeles",
        "zip_code": "90027",
        "country": "US",
        "state": "CA",
        "display_address": [
          "5270 Sunset Blvd",
          "Los Angeles, CA 90027"
        ]
      },
      "phone": "",
      "display_phone": "",
      "distance": 4289.288673948489
    },
    {
      "id": "8Gw1ISK7BT2MRapGxp5q5w",
      "alias": "cava-los-angeles-9",
      "name": "Cava",
      "image_url": "https://s3-media3.fl.yelpcdn.com/bphoto/HRe1GC5K1MNYt8PasBkr5A/o.jpg",
      "is_closed": False,
      "url": "https://www.yelp.com/biz/cava-los-angeles-9?adjust_creative=ZKhGl9Asv55quGIOH6hVeA&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=ZKhGl9Asv55quGIOH6hVeA",
      "review_count": 29,
      "categories": [
        {
          "alias": "mediterranean",
          "title": "Mediterranean"
        },
        {
          "alias": "desserts",
          "title": "Desserts"
        },
        {
          "alias": "salad",
          "title": "Salad"
        }
      ],
      "rating": 3.9,
      "coordinates": {
        "latitude": 34.09760108915641,
        "longitude": -118.3239478447302
      },
      "transactions": [],
      "location": {
        "address1": "6200 Sunset Blvd",
        "address2": "Ste 1130",
        "address3": None,
        "city": "Los Angeles",
        "zip_code": "90028",
        "country": "US",
        "state": "CA",
        "display_address": [
          "6200 Sunset Blvd",
          "Ste 1130",
          "Los Angeles, CA 90028"
        ]
      },
      "phone": "+12137822155",
      "display_phone": "(213) 782-2155",
      "distance": 4011.270914599968
    },
    {
      "id": "4JZK5nkIP6vKXdWNK8qXEg",
      "alias": "burger-she-wrote-los-angeles-2",
      "name": "Burger She Wrote",
      "image_url": "https://s3-media2.fl.yelpcdn.com/bphoto/uir6xZKUl-k41X1kcYnQHA/o.jpg",
      "is_closed": False,
      "url": "https://www.yelp.com/biz/burger-she-wrote-los-angeles-2?adjust_creative=ZKhGl9Asv55quGIOH6hVeA&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=ZKhGl9Asv55quGIOH6hVeA",
      "review_count": 283,
      "categories": [
        {
          "alias": "burgers",
          "title": "Burgers"
        }
      ],
      "rating": 3.8,
      "coordinates": {
        "latitude": 34.0760151,
        "longitude": -118.35244
      },
      "transactions": [],
      "price": "$$",
      "location": {
        "address1": "7454 1/2 Beverly Blvd",
        "address2": "",
        "address3": None,
        "city": "Los Angeles",
        "zip_code": "90036",
        "country": "US",
        "state": "CA",
        "display_address": [
          "7454 1/2 Beverly Blvd",
          "Los Angeles, CA 90036"
        ]
      },
      "phone": "+13232723474",
      "display_phone": "(323) 272-3474",
      "distance": 3280.4709120709385
    },
    {
      "id": "Gu2xyQvF0pph3Z7AcDZHAw",
      "alias": "the-original-hawowshi-los-angeles-4",
      "name": "The Original HaWOWshi",
      "image_url": "https://s3-media3.fl.yelpcdn.com/bphoto/xdoWCg_SChCDBDGzTdDlww/o.jpg",
      "is_closed": False,
      "url": "https://www.yelp.com/biz/the-original-hawowshi-los-angeles-4?adjust_creative=ZKhGl9Asv55quGIOH6hVeA&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=ZKhGl9Asv55quGIOH6hVeA",
      "review_count": 28,
      "categories": [
        {
          "alias": "egyptian",
          "title": "Egyptian"
        },
        {
          "alias": "foodtrucks",
          "title": "Food Trucks"
        }
      ],
      "rating": 4.9,
      "coordinates": {
        "latitude": 34.03068340237639,
        "longitude": -118.39953079144868
      },
      "transactions": [],
      "location": {
        "address1": None,
        "address2": None,
        "address3": "",
        "city": "Los Angeles ",
        "zip_code": "90034",
        "country": "US",
        "state": "CA",
        "display_address": [
          "Los Angeles , CA 90034"
        ]
      },
      "phone": "+18188261413",
      "display_phone": "(818) 826-1413",
      "distance": 7978.409930828185
    },
    {
      "id": "RMi8jn4ZBnAL3-l1T7tjmA",
      "alias": "alejandra-s-quesadilla-cart-los-angeles",
      "name": "Alejandra’s Quesadilla Cart",
      "image_url": "https://s3-media4.fl.yelpcdn.com/bphoto/5RH7-ZEYVQGVxMIVZD8JSw/o.jpg",
      "is_closed": False,
      "url": "https://www.yelp.com/biz/alejandra-s-quesadilla-cart-los-angeles?adjust_creative=ZKhGl9Asv55quGIOH6hVeA&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=ZKhGl9Asv55quGIOH6hVeA",
      "review_count": 177,
      "categories": [
        {
          "alias": "foodstands",
          "title": "Food Stands"
        },
        {
          "alias": "mexican",
          "title": "Mexican"
        }
      ],
      "rating": 4.6,
      "coordinates": {
        "latitude": 34.0760671,
        "longitude": -118.257599
      },
      "transactions": [],
      "price": "$",
      "location": {
        "address1": "1246 Echo Park Ave",
        "address2": "",
        "address3": "",
        "city": "Los Angeles",
        "zip_code": "90026",
        "country": "US",
        "state": "CA",
        "display_address": [
          "1246 Echo Park Ave",
          "Los Angeles, CA 90026"
        ]
      },
      "phone": "+13233833580",
      "display_phone": "(323) 383-3580",
      "distance": 6137.402384560244
    },
    {
      "id": "3mZU4RIAXNBwUEVF63bEHQ",
      "alias": "irvs-burgers-west-hollywood-4",
      "name": "Irv's Burgers",
      "image_url": "https://s3-media4.fl.yelpcdn.com/bphoto/tCoX9qIMftYOuLu7mE_Swg/o.jpg",
      "is_closed": False,
      "url": "https://www.yelp.com/biz/irvs-burgers-west-hollywood-4?adjust_creative=ZKhGl9Asv55quGIOH6hVeA&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=ZKhGl9Asv55quGIOH6hVeA",
      "review_count": 646,
      "categories": [
        {
          "alias": "burgers",
          "title": "Burgers"
        },
        {
          "alias": "sandwiches",
          "title": "Sandwiches"
        }
      ],
      "rating": 4.3,
      "coordinates": {
        "latitude": 34.090622,
        "longitude": -118.364698
      },
      "transactions": [],
      "price": "$$",
      "location": {
        "address1": "7998 Santa Monica Blvd",
        "address2": "",
        "address3": "",
        "city": "West Hollywood",
        "zip_code": "90046",
        "country": "US",
        "state": "CA",
        "display_address": [
          "7998 Santa Monica Blvd",
          "West Hollywood, CA 90046"
        ]
      },
      "phone": "+13239005677",
      "display_phone": "(323) 900-5677",
      "distance": 5136.288314510809
    },
    {
      "id": "Pg5rND7Xbnwm_sbhsnZThQ",
      "alias": "ggiata-west-hollywood-west-hollywood",
      "name": "Ggiata - West Hollywood",
      "image_url": "https://s3-media3.fl.yelpcdn.com/bphoto/RC-Xru85ivxmnfM_lOaYIQ/o.jpg",
      "is_closed": False,
      "url": "https://www.yelp.com/biz/ggiata-west-hollywood-west-hollywood?adjust_creative=ZKhGl9Asv55quGIOH6hVeA&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=ZKhGl9Asv55quGIOH6hVeA",
      "review_count": 123,
      "categories": [
        {
          "alias": "italian",
          "title": "Italian"
        },
        {
          "alias": "sandwiches",
          "title": "Sandwiches"
        }
      ],
      "rating": 4,
      "coordinates": {
        "latitude": 34.090645827659024,
        "longitude": -118.3647459
      },
      "transactions": [],
      "price": "$$",
      "location": {
        "address1": "7998 Santa Monica Blvd",
        "address2": None,
        "address3": "",
        "city": "West Hollywood",
        "zip_code": "90046",
        "country": "US",
        "state": "CA",
        "display_address": [
          "7998 Santa Monica Blvd",
          "West Hollywood, CA 90046"
        ]
      },
      "phone": "+13233805338",
      "display_phone": "(323) 380-5338",
      "distance": 5137.219981303642
    },
    {
      "id": "-5TFq3V--bffJGW000YuGQ",
      "alias": "holbox-los-angeles-2",
      "name": "Holbox",
      "image_url": "https://s3-media1.fl.yelpcdn.com/bphoto/f8OuY7bBbjY-rLR6qrC0lA/o.jpg",
      "is_closed": False,
      "url": "https://www.yelp.com/biz/holbox-los-angeles-2?adjust_creative=ZKhGl9Asv55quGIOH6hVeA&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=ZKhGl9Asv55quGIOH6hVeA",
      "review_count": 1175,
      "categories": [
        {
          "alias": "latin",
          "title": "Latin American"
        },
        {
          "alias": "seafood",
          "title": "Seafood"
        },
        {
          "alias": "mexican",
          "title": "Mexican"
        }
      ],
      "rating": 4.8,
      "coordinates": {
        "latitude": 34.01741823002926,
        "longitude": -118.27843182418148
      },
      "transactions": [
        "delivery",
        "pickup"
      ],
      "price": "$$",
      "location": {
        "address1": "3655 S Grand Ave",
        "address2": "Ste C9",
        "address3": None,
        "city": "Los Angeles",
        "zip_code": "90007",
        "country": "US",
        "state": "CA",
        "display_address": [
          "3655 S Grand Ave",
          "Ste C9",
          "Los Angeles, CA 90007"
        ]
      },
      "phone": "+12139869972",
      "display_phone": "(213) 986-9972",
      "distance": 6307.523660634909
    },
    {
      "id": "o_EwVCXB9BB_pxMULoLxeQ",
      "alias": "harucake-los-angeles",
      "name": "Harucake",
      "image_url": "https://s3-media2.fl.yelpcdn.com/bphoto/_S6KL888G8mPXRWW_j53WQ/o.jpg",
      "is_closed": False,
      "url": "https://www.yelp.com/biz/harucake-los-angeles?adjust_creative=ZKhGl9Asv55quGIOH6hVeA&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=ZKhGl9Asv55quGIOH6hVeA",
      "review_count": 346,
      "categories": [
        {
          "alias": "coffee",
          "title": "Coffee & Tea"
        },
        {
          "alias": "cakeshop",
          "title": "Patisserie/Cake Shop"
        }
      ],
      "rating": 4.2,
      "coordinates": {
        "latitude": 34.0631971,
        "longitude": -118.2971971
      },
      "transactions": [],
      "location": {
        "address1": "3450 W 6th St",
        "address2": "Ste 107",
        "address3": "",
        "city": "Los Angeles",
        "zip_code": "90020",
        "country": "US",
        "state": "CA",
        "display_address": [
          "3450 W 6th St",
          "Ste 107",
          "Los Angeles, CA 90020"
        ]
      },
      "phone": "+12133222060",
      "display_phone": "(213) 322-2060",
      "distance": 2234.8705739650945
    },
    {
      "id": "Y2_4gSj9r2pzktbkWZrlig",
      "alias": "lodge-bread-los-angeles-4",
      "name": "Lodge Bread",
      "image_url": "https://s3-media3.fl.yelpcdn.com/bphoto/eo7p-nBsgs4oBrM9M15qNA/o.jpg",
      "is_closed": False,
      "url": "https://www.yelp.com/biz/lodge-bread-los-angeles-4?adjust_creative=ZKhGl9Asv55quGIOH6hVeA&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=ZKhGl9Asv55quGIOH6hVeA",
      "review_count": 87,
      "categories": [
        {
          "alias": "bakeries",
          "title": "Bakeries"
        },
        {
          "alias": "sandwiches",
          "title": "Sandwiches"
        },
        {
          "alias": "breakfast_brunch",
          "title": "Breakfast & Brunch"
        }
      ],
      "rating": 4.5,
      "coordinates": {
        "latitude": 34.0533397,
        "longitude": -118.3769423
      },
      "transactions": [],
      "price": "$$",
      "location": {
        "address1": "8532 W Pico Blvd",
        "address2": None,
        "address3": "",
        "city": "Los Angeles",
        "zip_code": "90035",
        "country": "US",
        "state": "CA",
        "display_address": [
          "8532 W Pico Blvd",
          "Los Angeles, CA 90035"
        ]
      },
      "phone": "+14243020225",
      "display_phone": "(424) 302-0225",
      "distance": 5206.931359884714
    }
  ],
  "total": 15000,
  "region": {
    "center": {
      "longitude": -118.32138061523438,
      "latitude": 34.0615895441259
    }
  }
}
la_restaurants = la_data['businesses']
la_ids = []
la_names = []
for restaurant in la_restaurants:
    la_ids.append(restaurant['id'])
    la_names.append(restaurant['name'])

portland_data = {
  "businesses": [
    {
      "id": "Ys42wLKqrflqmtqkgqOXgA",
      "alias": "luc-lac-portland-7",
      "name": "Luc Lac",
      "image_url": "https://s3-media3.fl.yelpcdn.com/bphoto/MKhp6BM0esexFcD6OOKaeQ/o.jpg",
      "is_closed": False,
      "url": "https://www.yelp.com/biz/luc-lac-portland-7?adjust_creative=ZKhGl9Asv55quGIOH6hVeA&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=ZKhGl9Asv55quGIOH6hVeA",
      "review_count": 4308,
      "categories": [
        {
          "alias": "vietnamese",
          "title": "Vietnamese"
        },
        {
          "alias": "tapasmallplates",
          "title": "Tapas/Small Plates"
        },
        {
          "alias": "cocktailbars",
          "title": "Cocktail Bars"
        }
      ],
      "rating": 4.1,
      "coordinates": {
        "latitude": 45.516868,
        "longitude": -122.675447
      },
      "transactions": [
        "pickup",
        "delivery"
      ],
      "price": "$$",
      "location": {
        "address1": "835 SW 2nd Ave",
        "address2": None,
        "address3": "",
        "city": "Portland",
        "zip_code": "97204",
        "country": "US",
        "state": "OR",
        "display_address": [
          "835 SW 2nd Ave",
          "Portland, OR 97204"
        ]
      },
      "phone": "+15032220047",
      "display_phone": "(503) 222-0047",
      "distance": 1664.3957803786045
    },
    {
      "id": "pmXx9-xxOHTQJ22hHFD2GQ",
      "alias": "hansik-portland-6",
      "name": "Hansik",
      "image_url": "https://s3-media2.fl.yelpcdn.com/bphoto/d05oQkh_ELSV0BVRrbUFxQ/o.jpg",
      "is_closed": False,
      "url": "https://www.yelp.com/biz/hansik-portland-6?adjust_creative=ZKhGl9Asv55quGIOH6hVeA&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=ZKhGl9Asv55quGIOH6hVeA",
      "review_count": 22,
      "categories": [
        {
          "alias": "salad",
          "title": "Salad"
        },
        {
          "alias": "bbq",
          "title": "Barbeque"
        },
        {
          "alias": "korean",
          "title": "Korean"
        }
      ],
      "rating": 4.7,
      "coordinates": {
        "latitude": 45.485941,
        "longitude": -122.761261
      },
      "transactions": [],
      "location": {
        "address1": "8225 SW Apple Way",
        "address2": "Ste 102",
        "address3": "",
        "city": "Portland",
        "zip_code": "97225",
        "country": "US",
        "state": "OR",
        "display_address": [
          "8225 SW Apple Way",
          "Ste 102",
          "Portland, OR 97225"
        ]
      },
      "phone": "+19713865900",
      "display_phone": "(971) 386-5900",
      "distance": 8986.5172420225
    },
    {
      "id": "6DwR5rF1s6fJn4f-Lvfbuw",
      "alias": "eem-portland",
      "name": "Eem",
      "image_url": "https://s3-media2.fl.yelpcdn.com/bphoto/eITdDr4IffxkXCl980rG1w/o.jpg",
      "is_closed": False,
      "url": "https://www.yelp.com/biz/eem-portland?adjust_creative=ZKhGl9Asv55quGIOH6hVeA&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=ZKhGl9Asv55quGIOH6hVeA",
      "review_count": 1172,
      "categories": [
        {
          "alias": "cocktailbars",
          "title": "Cocktail Bars"
        },
        {
          "alias": "thai",
          "title": "Thai"
        },
        {
          "alias": "bbq",
          "title": "Barbeque"
        }
      ],
      "rating": 4.5,
      "coordinates": {
        "latitude": 45.55074523709471,
        "longitude": -122.66653193073176
      },
      "transactions": [
        "pickup",
        "delivery"
      ],
      "price": "$$",
      "location": {
        "address1": "3808 N Williams Ave",
        "address2": "Ste 127",
        "address3": None,
        "city": "Portland",
        "zip_code": "97227",
        "country": "US",
        "state": "OR",
        "display_address": [
          "3808 N Williams Ave",
          "Ste 127",
          "Portland, OR 97227"
        ]
      },
      "phone": "+19712951645",
      "display_phone": "(971) 295-1645",
      "distance": 4005.8853149197994
    },
    {
      "id": "6VhcvzGrfYYSygc9UKYfQw",
      "alias": "nongs-khao-man-gai-portland-2",
      "name": "Nong's Khao Man Gai",
      "image_url": "https://s3-media2.fl.yelpcdn.com/bphoto/cJ26J00XztbtV3MisZorfw/o.jpg",
      "is_closed": False,
      "url": "https://www.yelp.com/biz/nongs-khao-man-gai-portland-2?adjust_creative=ZKhGl9Asv55quGIOH6hVeA&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=ZKhGl9Asv55quGIOH6hVeA",
      "review_count": 2246,
      "categories": [
        {
          "alias": "thai",
          "title": "Thai"
        },
        {
          "alias": "chickenshop",
          "title": "Chicken Shop"
        },
        {
          "alias": "cocktailbars",
          "title": "Cocktail Bars"
        }
      ],
      "rating": 4.3,
      "coordinates": {
        "latitude": 45.52235,
        "longitude": -122.6595
      },
      "transactions": [
        "pickup",
        "delivery"
      ],
      "price": "$$",
      "location": {
        "address1": "609 SE Ankeny St",
        "address2": "Ste C",
        "address3": "",
        "city": "Portland",
        "zip_code": "97214",
        "country": "US",
        "state": "OR",
        "display_address": [
          "609 SE Ankeny St",
          "Ste C",
          "Portland, OR 97214"
        ]
      },
      "phone": "+15037402907",
      "display_phone": "(503) 740-2907",
      "distance": 839.3773667172169
    },
    {
      "id": "bO2ADMWH8gNUbNxcLNdPNA",
      "alias": "tokyo-sando-portland-3",
      "name": "Tokyo Sando",
      "image_url": "https://s3-media3.fl.yelpcdn.com/bphoto/tolHcvMQ0MQeAdmQ4EpZbw/o.jpg",
      "is_closed": False,
      "url": "https://www.yelp.com/biz/tokyo-sando-portland-3?adjust_creative=ZKhGl9Asv55quGIOH6hVeA&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=ZKhGl9Asv55quGIOH6hVeA",
      "review_count": 342,
      "categories": [
        {
          "alias": "japanese",
          "title": "Japanese"
        },
        {
          "alias": "sandwiches",
          "title": "Sandwiches"
        },
        {
          "alias": "foodtrucks",
          "title": "Food Trucks"
        }
      ],
      "rating": 4.6,
      "coordinates": {
        "latitude": 45.52087246448454,
        "longitude": -122.67610667054348
      },
      "transactions": [
        "delivery"
      ],
      "price": "$$",
      "location": {
        "address1": "431 SW Harvey Milk St",
        "address2": None,
        "address3": "",
        "city": "Portland",
        "zip_code": "97204",
        "country": "US",
        "state": "OR",
        "display_address": [
          "431 SW Harvey Milk St",
          "Portland, OR 97204"
        ]
      },
      "phone": "+19712543744",
      "display_phone": "(971) 254-3744",
      "distance": 1804.4646505103303
    },
    {
      "id": "8ngTOtcoDUKGNMnCQ9NwHA",
      "alias": "xin-ding-dumpling-house-portland",
      "name": "Xin Ding Dumpling House",
      "image_url": "https://s3-media1.fl.yelpcdn.com/bphoto/zYCaPNpAAy7Vc-74SrVL8A/o.jpg",
      "is_closed": False,
      "url": "https://www.yelp.com/biz/xin-ding-dumpling-house-portland?adjust_creative=ZKhGl9Asv55quGIOH6hVeA&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=ZKhGl9Asv55quGIOH6hVeA",
      "review_count": 147,
      "categories": [
        {
          "alias": "dimsum",
          "title": "Dim Sum"
        },
        {
          "alias": "noodles",
          "title": "Noodles"
        },
        {
          "alias": "hotpot",
          "title": "Hot Pot"
        }
      ],
      "rating": 4.3,
      "coordinates": {
        "latitude": 45.522254380028194,
        "longitude": -122.6724998020494
      },
      "transactions": [
        "pickup",
        "delivery"
      ],
      "price": "$$",
      "location": {
        "address1": "71 SW 2nd Ave",
        "address2": "",
        "address3": None,
        "city": "Portland",
        "zip_code": "97204",
        "country": "US",
        "state": "OR",
        "display_address": [
          "71 SW 2nd Ave",
          "Portland, OR 97204"
        ]
      },
      "phone": "+15033457777",
      "display_phone": "(503) 345-7777",
      "distance": 1602.936923291129
    },
    {
      "id": "OQ2oHkcWA8KNC1Lsvj1SBA",
      "alias": "screen-door-eastside-portland-3",
      "name": "Screen Door Eastside",
      "image_url": "https://s3-media2.fl.yelpcdn.com/bphoto/UkYD582pg4fPlO1_spvgEQ/o.jpg",
      "is_closed": False,
      "url": "https://www.yelp.com/biz/screen-door-eastside-portland-3?adjust_creative=ZKhGl9Asv55quGIOH6hVeA&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=ZKhGl9Asv55quGIOH6hVeA",
      "review_count": 8538,
      "categories": [
        {
          "alias": "southern",
          "title": "Southern"
        },
        {
          "alias": "cajun",
          "title": "Cajun/Creole"
        },
        {
          "alias": "breakfast_brunch",
          "title": "Breakfast & Brunch"
        }
      ],
      "rating": 4.5,
      "coordinates": {
        "latitude": 45.523052,
        "longitude": -122.641665
      },
      "transactions": [
        "pickup",
        "delivery"
      ],
      "price": "$$",
      "location": {
        "address1": "2337 E Burnside St",
        "address2": None,
        "address3": "",
        "city": "Portland",
        "zip_code": "97214",
        "country": "US",
        "state": "OR",
        "display_address": [
          "2337 E Burnside St",
          "Portland, OR 97214"
        ]
      },
      "phone": "+15035420880",
      "display_phone": "(503) 542-0880",
      "distance": 1263.8780258971117
    },
    {
      "id": "fxTwO4KSP05chyZTBva2GA",
      "alias": "obon-shokudo-portland",
      "name": "Obon Shokudo",
      "image_url": "https://s3-media3.fl.yelpcdn.com/bphoto/MZlBqdL7mFY1CaojbJrWJQ/o.jpg",
      "is_closed": False,
      "url": "https://www.yelp.com/biz/obon-shokudo-portland?adjust_creative=ZKhGl9Asv55quGIOH6hVeA&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=ZKhGl9Asv55quGIOH6hVeA",
      "review_count": 192,
      "categories": [
        {
          "alias": "japanese",
          "title": "Japanese"
        },
        {
          "alias": "vegan",
          "title": "Vegan"
        },
        {
          "alias": "comfortfood",
          "title": "Comfort Food"
        }
      ],
      "rating": 4.5,
      "coordinates": {
        "latitude": 45.5175717,
        "longitude": -122.66056064253196
      },
      "transactions": [
        "delivery"
      ],
      "price": "$$",
      "location": {
        "address1": "720 SE Grand Ave",
        "address2": None,
        "address3": "",
        "city": "Portland",
        "zip_code": "97214",
        "country": "US",
        "state": "OR",
        "display_address": [
          "720 SE Grand Ave",
          "Portland, OR 97214"
        ]
      },
      "phone": "+15032067967",
      "display_phone": "(503) 206-7967",
      "distance": 540.1502878496384
    },
    {
      "id": "3MIhYQRC6XUKZjIZbxRrYA",
      "alias": "bao-bao-portland-2",
      "name": "Bao Bao",
      "image_url": "https://s3-media4.fl.yelpcdn.com/bphoto/p1Q-UHd0P9iodAsAU1l4lA/o.jpg",
      "is_closed": False,
      "url": "https://www.yelp.com/biz/bao-bao-portland-2?adjust_creative=ZKhGl9Asv55quGIOH6hVeA&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=ZKhGl9Asv55quGIOH6hVeA",
      "review_count": 390,
      "categories": [
        {
          "alias": "chinese",
          "title": "Chinese"
        },
        {
          "alias": "comfortfood",
          "title": "Comfort Food"
        },
        {
          "alias": "hotdogs",
          "title": "Fast Food"
        }
      ],
      "rating": 4.3,
      "coordinates": {
        "latitude": 45.523738,
        "longitude": -122.6599677
      },
      "transactions": [
        "pickup",
        "delivery"
      ],
      "price": "$$",
      "location": {
        "address1": "545 NE Couch St",
        "address2": None,
        "address3": "",
        "city": "Portland",
        "zip_code": "97232",
        "country": "US",
        "state": "OR",
        "display_address": [
          "545 NE Couch St",
          "Portland, OR 97232"
        ]
      },
      "phone": "+15034778911",
      "display_phone": "(503) 477-8911",
      "distance": 994.9747620161661
    },
    {
      "id": "fP45Ns78xlfeAs2ouHklOg",
      "alias": "cheryl-s-on-12th-portland",
      "name": "Cheryl’s on 12th",
      "image_url": "https://s3-media3.fl.yelpcdn.com/bphoto/5H1raFuS4OTa7-oR0iX0Gw/o.jpg",
      "is_closed": False,
      "url": "https://www.yelp.com/biz/cheryl-s-on-12th-portland?adjust_creative=ZKhGl9Asv55quGIOH6hVeA&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=ZKhGl9Asv55quGIOH6hVeA",
      "review_count": 2659,
      "categories": [
        {
          "alias": "breakfast_brunch",
          "title": "Breakfast & Brunch"
        },
        {
          "alias": "sandwiches",
          "title": "Sandwiches"
        },
        {
          "alias": "newamerican",
          "title": "New American"
        }
      ],
      "rating": 4.4,
      "coordinates": {
        "latitude": 45.521926,
        "longitude": -122.683228
      },
      "transactions": [
        "pickup",
        "delivery"
      ],
      "price": "$$",
      "location": {
        "address1": "1135 SW Washington St",
        "address2": "",
        "address3": "",
        "city": "Portland",
        "zip_code": "97205",
        "country": "US",
        "state": "OR",
        "display_address": [
          "1135 SW Washington St",
          "Portland, OR 97205"
        ]
      },
      "phone": "+15035952252",
      "display_phone": "(503) 595-2252",
      "distance": 2368.8685584447594
    },
    {
      "id": "5oed6H5F8qZxNzELq_1e1w",
      "alias": "pine-state-biscuits-portland-2",
      "name": "Pine State Biscuits",
      "image_url": "https://s3-media3.fl.yelpcdn.com/bphoto/d0caJPwd1GhDlDtmrF_7Pw/o.jpg",
      "is_closed": False,
      "url": "https://www.yelp.com/biz/pine-state-biscuits-portland-2?adjust_creative=ZKhGl9Asv55quGIOH6hVeA&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=ZKhGl9Asv55quGIOH6hVeA",
      "review_count": 4142,
      "categories": [
        {
          "alias": "southern",
          "title": "Southern"
        },
        {
          "alias": "breakfast_brunch",
          "title": "Breakfast & Brunch"
        },
        {
          "alias": "sandwiches",
          "title": "Sandwiches"
        }
      ],
      "rating": 4.3,
      "coordinates": {
        "latitude": 45.55900397395001,
        "longitude": -122.64273832072884
      },
      "transactions": [
        "pickup",
        "delivery"
      ],
      "price": "$$",
      "location": {
        "address1": "2204 NE Alberta St",
        "address2": None,
        "address3": "",
        "city": "Portland",
        "zip_code": "97211",
        "country": "US",
        "state": "OR",
        "display_address": [
          "2204 NE Alberta St",
          "Portland, OR 97211"
        ]
      },
      "phone": "+15034776605",
      "display_phone": "(503) 477-6605",
      "distance": 4886.669631570108
    },
    {
      "id": "lwtQddUwAKyQLvKr9PRcOA",
      "alias": "stretch-the-noodle-portland-3",
      "name": "Stretch the Noodle",
      "image_url": "https://s3-media3.fl.yelpcdn.com/bphoto/alr5RodHdSgsHpQDmheoUQ/o.jpg",
      "is_closed": False,
      "url": "https://www.yelp.com/biz/stretch-the-noodle-portland-3?adjust_creative=ZKhGl9Asv55quGIOH6hVeA&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=ZKhGl9Asv55quGIOH6hVeA",
      "review_count": 477,
      "categories": [
        {
          "alias": "noodles",
          "title": "Noodles"
        },
        {
          "alias": "chinese",
          "title": "Chinese"
        },
        {
          "alias": "foodstands",
          "title": "Food Stands"
        }
      ],
      "rating": 4.3,
      "coordinates": {
        "latitude": 45.52095,
        "longitude": -122.67598
      },
      "transactions": [],
      "price": "$$",
      "location": {
        "address1": "431 SW Harvey Milk St",
        "address2": None,
        "address3": None,
        "city": "Portland",
        "zip_code": "97204",
        "country": "US",
        "state": "OR",
        "display_address": [
          "431 SW Harvey Milk St",
          "Portland, OR 97204"
        ]
      },
      "phone": "",
      "display_phone": "",
      "distance": 1803.9082206136118
    },
    {
      "id": "eOseyvtaFHwVKAS0GePV4g",
      "alias": "808-grinds-hawaiian-cafe-portland-2",
      "name": "808 Grinds Hawaiian Cafe",
      "image_url": "https://s3-media3.fl.yelpcdn.com/bphoto/PtIrmSrS4CXMYLM7zSBhxA/o.jpg",
      "is_closed": False,
      "url": "https://www.yelp.com/biz/808-grinds-hawaiian-cafe-portland-2?adjust_creative=ZKhGl9Asv55quGIOH6hVeA&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=ZKhGl9Asv55quGIOH6hVeA",
      "review_count": 756,
      "categories": [
        {
          "alias": "hawaiian",
          "title": "Hawaiian"
        }
      ],
      "rating": 4.5,
      "coordinates": {
        "latitude": 45.5068486974626,
        "longitude": -122.780843906607
      },
      "transactions": [
        "delivery"
      ],
      "price": "$$",
      "location": {
        "address1": "10100 SW Park Way",
        "address2": "",
        "address3": "",
        "city": "Portland",
        "zip_code": "97225",
        "country": "US",
        "state": "OR",
        "display_address": [
          "10100 SW Park Way",
          "Portland, OR 97225"
        ]
      },
      "phone": "+15034779976",
      "display_phone": "(503) 477-9976",
      "distance": 9924.911734740026
    },
    {
      "id": "mw0-ONI4Qz-TELzJKrZbgQ",
      "alias": "cartopia-food-carts-portland",
      "name": "Cartopia Food Carts",
      "image_url": "https://s3-media4.fl.yelpcdn.com/bphoto/86jXaqDrSWTCQFkyDs9RQg/o.jpg",
      "is_closed": False,
      "url": "https://www.yelp.com/biz/cartopia-food-carts-portland?adjust_creative=ZKhGl9Asv55quGIOH6hVeA&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=ZKhGl9Asv55quGIOH6hVeA",
      "review_count": 176,
      "categories": [
        {
          "alias": "foodtrucks",
          "title": "Food Trucks"
        }
      ],
      "rating": 4.3,
      "coordinates": {
        "latitude": 45.51244823609407,
        "longitude": -122.6533979136289
      },
      "transactions": [
        "delivery"
      ],
      "price": "$$",
      "location": {
        "address1": "1207 SE Hawthorne Blvd",
        "address2": "",
        "address3": "",
        "city": "Portland",
        "zip_code": "97214",
        "country": "US",
        "state": "OR",
        "display_address": [
          "1207 SE Hawthorne Blvd",
          "Portland, OR 97214"
        ]
      },
      "phone": "",
      "display_phone": "",
      "distance": 375.2436641056086
    },
    {
      "id": "QrvhRSVPAuRLeIXcnnCGKQ",
      "alias": "yokohama-skyline-eatery-portland",
      "name": "Yokohama Skyline Eatery",
      "image_url": "https://s3-media3.fl.yelpcdn.com/bphoto/--ICt9zMCUeJnzhCX0Goug/o.jpg",
      "is_closed": False,
      "url": "https://www.yelp.com/biz/yokohama-skyline-eatery-portland?adjust_creative=ZKhGl9Asv55quGIOH6hVeA&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=ZKhGl9Asv55quGIOH6hVeA",
      "review_count": 57,
      "categories": [
        {
          "alias": "ramen",
          "title": "Ramen"
        }
      ],
      "rating": 4.7,
      "coordinates": {
        "latitude": 45.5234165127324,
        "longitude": -122.663142
      },
      "transactions": [
        "pickup",
        "delivery"
      ],
      "price": "$$",
      "location": {
        "address1": "33 NE 3rd Ave",
        "address2": "Ste 325",
        "address3": "",
        "city": "Portland",
        "zip_code": "97232",
        "country": "US",
        "state": "OR",
        "display_address": [
          "33 NE 3rd Ave",
          "Ste 325",
          "Portland, OR 97232"
        ]
      },
      "phone": "+15032064513",
      "display_phone": "(503) 206-4513",
      "distance": 1102.171370034147
    },
    {
      "id": "k3FzKinhC-dAGdhJGSXl_w",
      "alias": "khao-moo-dang-portland-3",
      "name": "Khao Moo Dang",
      "image_url": "https://s3-media1.fl.yelpcdn.com/bphoto/7Hn6pDrnRDeKHx-wUXjkJA/o.jpg",
      "is_closed": False,
      "url": "https://www.yelp.com/biz/khao-moo-dang-portland-3?adjust_creative=ZKhGl9Asv55quGIOH6hVeA&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=ZKhGl9Asv55quGIOH6hVeA",
      "review_count": 372,
      "categories": [
        {
          "alias": "thai",
          "title": "Thai"
        },
        {
          "alias": "comfortfood",
          "title": "Comfort Food"
        },
        {
          "alias": "noodles",
          "title": "Noodles"
        }
      ],
      "rating": 4.7,
      "coordinates": {
        "latitude": 45.512252,
        "longitude": -122.6328667
      },
      "transactions": [
        "pickup",
        "delivery"
      ],
      "price": "$$",
      "location": {
        "address1": "3145 SE Hawthorne Blvd",
        "address2": None,
        "address3": "",
        "city": "Portland",
        "zip_code": "97214",
        "country": "US",
        "state": "OR",
        "display_address": [
          "3145 SE Hawthorne Blvd",
          "Portland, OR 97214"
        ]
      },
      "phone": "+15032066838",
      "display_phone": "(503) 206-6838",
      "distance": 1701.5133962647774
    },
    {
      "id": "UzL82EkUoXQRExf8DJD-sQ",
      "alias": "kubo-portland",
      "name": "Kubo",
      "image_url": "https://s3-media3.fl.yelpcdn.com/bphoto/MVXqqmYszbxNiVmR9q6qsA/o.jpg",
      "is_closed": False,
      "url": "https://www.yelp.com/biz/kubo-portland?adjust_creative=ZKhGl9Asv55quGIOH6hVeA&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=ZKhGl9Asv55quGIOH6hVeA",
      "review_count": 78,
      "categories": [
        {
          "alias": "filipino",
          "title": "Filipino"
        }
      ],
      "rating": 4.7,
      "coordinates": {
        "latitude": 45.554187,
        "longitude": -122.836032
      },
      "transactions": [
        "pickup",
        "delivery"
      ],
      "location": {
        "address1": "4708 NW Bethany Blvd",
        "address2": "Ste E-8",
        "address3": "",
        "city": "Portland",
        "zip_code": "97229",
        "country": "US",
        "state": "OR",
        "display_address": [
          "4708 NW Bethany Blvd",
          "Ste E-8",
          "Portland, OR 97229"
        ]
      },
      "phone": "+15037464626",
      "display_phone": "(503) 746-4626",
      "distance": 14794.60827008364
    },
    {
      "id": "eUbq0uNxRlXQ6sy7phM7yA",
      "alias": "lechon-portland",
      "name": "Lechon",
      "image_url": "https://s3-media1.fl.yelpcdn.com/bphoto/octeLBKuX_M4qmupNJRiaA/o.jpg",
      "is_closed": False,
      "url": "https://www.yelp.com/biz/lechon-portland?adjust_creative=ZKhGl9Asv55quGIOH6hVeA&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=ZKhGl9Asv55quGIOH6hVeA",
      "review_count": 1945,
      "categories": [
        {
          "alias": "tapas",
          "title": "Tapas Bars"
        },
        {
          "alias": "cocktailbars",
          "title": "Cocktail Bars"
        },
        {
          "alias": "vegetarian",
          "title": "Vegetarian"
        }
      ],
      "rating": 4.5,
      "coordinates": {
        "latitude": 45.52129,
        "longitude": -122.67094
      },
      "transactions": [
        "delivery"
      ],
      "price": "$$$",
      "location": {
        "address1": "113 SW Naito Pkwy",
        "address2": None,
        "address3": "",
        "city": "Portland",
        "zip_code": "97204",
        "country": "US",
        "state": "OR",
        "display_address": [
          "113 SW Naito Pkwy",
          "Portland, OR 97204"
        ]
      },
      "phone": "+15032199000",
      "display_phone": "(503) 219-9000",
      "distance": 1435.8142462345995
    },
    {
      "id": "sJsccWG0XZAZIm6zI8I20w",
      "alias": "screen-door-pearl-district-portland",
      "name": "Screen Door Pearl District",
      "image_url": "https://s3-media3.fl.yelpcdn.com/bphoto/KzvXL-umwlA48mp7fd8dNQ/o.jpg",
      "is_closed": False,
      "url": "https://www.yelp.com/biz/screen-door-pearl-district-portland?adjust_creative=ZKhGl9Asv55quGIOH6hVeA&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=ZKhGl9Asv55quGIOH6hVeA",
      "review_count": 887,
      "categories": [
        {
          "alias": "southern",
          "title": "Southern"
        },
        {
          "alias": "breakfast_brunch",
          "title": "Breakfast & Brunch"
        },
        {
          "alias": "cajun",
          "title": "Cajun/Creole"
        }
      ],
      "rating": 4.5,
      "coordinates": {
        "latitude": 45.52379,
        "longitude": -122.68274
      },
      "transactions": [
        "delivery"
      ],
      "price": "$$",
      "location": {
        "address1": "1131 NW Couch St",
        "address2": "",
        "address3": None,
        "city": "Portland",
        "zip_code": "97209",
        "country": "US",
        "state": "OR",
        "display_address": [
          "1131 NW Couch St",
          "Portland, OR 97209"
        ]
      },
      "phone": "+15035420882",
      "display_phone": "(503) 542-0882",
      "distance": 2398.116224817019
    },
    {
      "id": "GgDKxGZBmzdyWmExESK14g",
      "alias": "the-observatory-portland",
      "name": "The Observatory",
      "image_url": "https://s3-media1.fl.yelpcdn.com/bphoto/adD5BZMTFejak_PL7MX-fA/o.jpg",
      "is_closed": False,
      "url": "https://www.yelp.com/biz/the-observatory-portland?adjust_creative=ZKhGl9Asv55quGIOH6hVeA&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=ZKhGl9Asv55quGIOH6hVeA",
      "review_count": 2366,
      "categories": [
        {
          "alias": "newamerican",
          "title": "New American"
        },
        {
          "alias": "lounges",
          "title": "Lounges"
        }
      ],
      "rating": 4.3,
      "coordinates": {
        "latitude": 45.519263,
        "longitude": -122.580217
      },
      "transactions": [
        "delivery"
      ],
      "price": "$$",
      "location": {
        "address1": "8115 SE Stark St",
        "address2": "",
        "address3": "",
        "city": "Portland",
        "zip_code": "97215",
        "country": "US",
        "state": "OR",
        "display_address": [
          "8115 SE Stark St",
          "Portland, OR 97215"
        ]
      },
      "phone": "+15034456284",
      "display_phone": "(503) 445-6284",
      "distance": 5770.505086556957
    }
  ],
  "total": 11900,
  "region": {
    "center": {
      "longitude": -122.65411376953125,
      "latitude": 45.515785397030584
    }
  }
}
portland_restaurants = portland_data['businesses']
portland_ids = []
portland_names = []
for restaurant in portland_restaurants:
    portland_ids.append(restaurant['id'])
    portland_names.append(restaurant['name'])


