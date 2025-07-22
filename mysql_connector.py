import pymysql
from config import MYSQL_CONFIG, PAGE_SIZE

def _conn():
    return pymysql.connect(**MYSQL_CONFIG,
                           cursorclass=pymysql.cursors.DictCursor,
                           autocommit=True)

def list_genres():
    with _conn() as c, c.cursor() as cur:
        cur.execute("SELECT name FROM category ORDER BY name;")
        return [r["name"] for r in cur.fetchall()]

def year_bounds():
    with _conn() as c, c.cursor() as cur:
        cur.execute("SELECT MIN(release_year) min_y, MAX(release_year) max_y FROM film;")
        return cur.fetchone()

def search_by_keyword(keyword: str, limit=PAGE_SIZE, offset=0):
    sql = """
        SELECT f.film_id, f.title, f.release_year,
               GROUP_CONCAT(c.name SEPARATOR ', ') genres
        FROM film f
        JOIN film_category fc ON f.film_id = fc.film_id
        JOIN category c       ON c.category_id = fc.category_id
        WHERE LOWER(f.title) LIKE %s
        GROUP BY f.film_id
        ORDER BY f.title
        LIMIT %s OFFSET %s;
    """
    with _conn() as c, c.cursor() as cur:
        cur.execute(sql, (f"%{keyword.lower()}%", limit, offset))
        return cur.fetchall()

def search_by_genre_year(genre: str, y1: int, y2: int,
                         limit=PAGE_SIZE, offset=0):
    sql = """
        SELECT f.film_id, f.title, f.release_year
        FROM film f
        JOIN film_category fc ON f.film_id = fc.film_id
        JOIN category c       ON c.category_id = fc.category_id
        WHERE c.name = %s
          AND f.release_year BETWEEN %s AND %s
        ORDER BY f.title
        LIMIT %s OFFSET %s;
    """
    with _conn() as c, c.cursor() as cur:
        cur.execute(sql, (genre, y1, y2, limit, offset))
        return cur.fetchall()