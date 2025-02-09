# Usage

[image](.src/images/toy.png)

- 모든 칸을 입력해야만 작동합니다.
- 이름 입력시 전체 이름 혹은 키워드 연속 된 이름 입력만 가능합니다 <br\>ex: Jordan 1 retro black toe -> jordan 1 혹은 black toe 혹은 1 retro
- off-white 제품 검색시 off-white "-" 넣어서 검색해야 합니다 



``` 
Usage: cob-t [OPTIONS] KEYWORD ASORDE WOTBY

╭─ Arguments ──────────────────────────────────────────────╮
│ *    keyword      TEXT  [default: None] [required]       │
│ *    asorde             [default: None] [required]       │
│ *    wotby        TEXT  [default: None] [required]       │
╰──────────────────────────────────────────────────────────╯
╭─ Options ────────────────────────────────────────────────╮
│ --help          Show this message and exit.              │
╰──────────────────────────────────────────────────────────╯


$ cob-t "eminem" False "highest_price"

                                name  sales retail_price  average_sale_price  highest_price  lowest_price release_date
      Jordan 4 Retro Eminem Carhartt      3                             8833          10500          7000   11/23/2015
Jordan 2 Retro Eminem (The Way I Am)      9          110                3249           4999          2700   12/18/2008
```

```
$ cob-t "jordan 1 retro" False "average_sale_price"
```

- "찾을 신발 이름" jordan 1 retro"(ex : jordan 3,jordan 5 retro)<br/>혹은 닉네임 키워드로 검색가능(ex : black toe,chicago)
- 평균리세일가격 내림차순으로 볼 경우 Fasle 오름차순으로 볼경우 True 입력
- "average_sale_price" wotby 자리에 입력 시 평균 리세일 가격 기준 출력<br/>"highest_price" 입력시 최고액 판매가 기준 출력 
- 금액은 USD $ 입니다.


# 🗂️ Create Table
- PostgreSQL:
```
CREATE TABLE ajs (
	name varchar NOT NULL,
        sales int NOT NULL,
	retail_price int NOT NULL,
	averge_sale_price int NOT NULL,
	highest_price int NOT NULL,
	lowest_price int NOT NULL,
	release_date varchar NOT NULL,
	CONSTRAINT ajs_pk PRIMARY KEY (name),
	CONSTRAINT ajs_unique UNIQUE (name)
);
```
- SQL
```
select * from ajs;
delete from ajs;

```
# Dev
```
$ source .venv/bin/activate
$ pdm add pandas
$ pdm add -dG eda jupyterlab
$ pdm add streamlit
$ pdm add "psycopg[binary,pool]"
$ pdm add python-dotenv
```
## DB관리
```
$ sudo docker ps -a
$ sudo docker start local-postgres
$ sudo docker stop local-postgres

# Into CONTAINER
$ sudo docker exec -it local-postgres bash
```

# Ref
- [kaggle.com/kailingding](https://www.kaggle.com/datasets/kailingding/air-jordans-on-stockx)



# CobsTicketToy
First project of my toy project<br/>It's about my hobby 


