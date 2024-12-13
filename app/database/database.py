import jaydebeapi

H2_URL = "jdbc:h2:mem:testdb"
H2_USERNAME = "1"
H2_PASSWORD = "1"
H2_JAR_PATH = "jar/h2-2.3.230.jar"
H2_DRIVER = "org.h2.Driver"

def get_db_connection():
    conn = jaydebeapi.connect(
        H2_DRIVER,
        H2_URL,
        [H2_USERNAME, H2_PASSWORD],
        H2_JAR_PATH
    )
    return conn