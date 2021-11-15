import redshift_connector

# Connects to Redshift cluster using AWS credentials
def redshift_connect(query1):
    conn = redshift_connector.connect(
    host='bhargav-redshift-cluster-1.cokuuopwai1b.us-east-1.redshift.amazonaws.com',
    database='dev',
    user='xxx',
    password='xxx'
    )
    cursor: redshift_connector.Cursor = conn.cursor()
    cursor.execute(query1)
    conn.commit()
    cursor.execute("select * from public.queue_output")
    result: tuple = cursor.fetchall()
    print(result)
#redshift_connect('''insert into public.queue_output values('124','task1','test','12','inprogress')''')
