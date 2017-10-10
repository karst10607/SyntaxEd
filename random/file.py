import pymysql.cursors
import os.path

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='sunya',
                             password='123456',
                             db='syntaxed')

try:
    path = 'C:/Users/Sunya/Downloads/db_POS'
    names = [name for name in os.listdir(path)
        if os.path.isfile(os.path.join(path, name))]

    #"""
    #Create tables use file name
    with connection.cursor() as cursor:        
        for name in names:
            #print(name[0:-5])
            sql = "CREATE TABLE `syntaxed`." + name[0:-5] + " ( `id` INT NOT NULL , `string` VARCHAR(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL )"
            cursor.execute(sql)
        connection.commit()
    #"""    

    #Insert text files of strings
    with connection.cursor() as cursor:  
        for name in names:
            cnt = 0
            with open(os.path.join(path, name)) as f:
                for line in f:
                    cnt+=1
                    sql = "INSERT INTO `" + name[0:-5] + "` (`id`, `string`) VALUES (" + str(cnt) + ", '" + line.strip() + "')"
                    if line.strip()!="": 
                        cursor.execute(sql)
                        print('Insert '+line.strip()+' success!')
                        #print(sql)
            connection.commit()

    #with connection.cursor() as cursor:
        # Create a new record
    #    sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
    #    cursor.execute(sql, ('webmaster@python.org', 'very-secret'))

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    #connection.commit()

    #with connection.cursor() as cursor:
        # Read a single record
    #    sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
    #    cursor.execute(sql, ('webmaster@python.org',))
    #    result = cursor.fetchone()
    #    print(result)
finally:
    connection.close()