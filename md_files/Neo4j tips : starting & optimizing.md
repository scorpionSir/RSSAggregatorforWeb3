# Neo4j tips : starting & optimizing¶

This article is a collection of tips and informations that I found useful to
know about neo4j, when learning about it. It also presents some performance
tips (from the developer point of view).

To start, read the [refcard](http://neo4j.com/docs/stable/cypher-refcard/),
and try using the web interface at
[http://localhost:7474](http://localhost:7474/).

## Py2neo¶

Example script that uses py2neo. It can be used to create benchmarks :

    
    
    import datetime
    from py2neo import Graph
    
    def bench(query, count, reset=True):
        graph = Graph()
    
        if reset:
            graph.cypher.run("MATCH (n) OPTIONAL MATCH (n)-[r]-() DELETE n,r")
            graph.cypher.run("CREATE CONSTRAINT ON (node:Node) ASSERT node.number IS UNIQUE")
            graph.cypher.run("CREATE (r:Root)")
    
        start = datetime.datetime.now()
        tx = graph.cypher.begin()
        for i in range(count):
            tx.append(query, {'i': i})
        tx.commit()
    
        print('---')
        print('query : %s' % query)
        print("%i queries. %s/second." % (count, count // (datetime.datetime.now() - start).total_seconds()))
    
    if __name__ == '__main__':
        bench("MATCH (:Root)-[:Child]->(n:Node {number: {i}}) RETURN n.count", 1000)
        bench("CREATE (:Root)-[:Child]->(:Node {number: {i}, count: 1})", 1000)
        bench("MATCH (root:Root) CREATE (root)-[:Child]->(:Node {number: {i}, count: 1})", 1000)
        bench("MATCH (root:Root) MERGE (root)-[:Child]->(n:Node {number: {i}}) ON CREATE SET n.count = 1 ON MATCH SET n.count = n.count + 1", 1000)
        bench("MATCH (root:Root)-[:Child]->(n:Node {number: {i}}) SET n.count = n.count + 1", 1000)
        bench("MATCH (root:Root) CREATE UNIQUE (root)-[:Child]->(n:Node {number: {i}}) SET n.count = coalesce(n.count, 0) + 1", 1000)
    

When you use py2neo, if you know that some requests can take a long time you
have to put that at the top of your script :

    
    
    from py2neo.packages.httpstream import http
    http.socket_timeout = 9999
    

If you don’t do that, after one minute or so the HTTP request will timeout…

With the py2neo Cypher API, the functions I used were:

>   * transactions: with the
> [begin](http://py2neo.org/2.0/cypher.html#py2neo.cypher.CypherResource.begin)
> function to get a
> [transaction](http://py2neo.org/2.0/cypher.html#transactions) object.
>
>   *
> [execute_one](http://py2neo.org/2.0/cypher.html#py2neo.cypher.CypherResource.execute_one)
> (if the query returns only one column and one row)
>
>   *
> [stream](http://py2neo.org/2.0/cypher.html#py2neo.cypher.CypherResource.stream)
> (if the query returns multiple columns/rows)
>
>   *
> [run](http://py2neo.org/2.0/cypher.html#py2neo.cypher.CypherResource.run)
> (if the query don’t return anything. If you do it multiple time, use a
> transaction instead !)
>
>

## Queries performance¶

The most important thing to know (also true with classic RDBMS) : each time
you do a query, it has to be sent to the server, parsed… So try to group them
using transactions. In particular, if you want to do a lot of queries to
write/modify items, transactions will lead to a HUGE improvement in
performance, as there is only one `sync()` to the disk per transaction.

You should also use [parameters](http://neo4j.com/docs/stable/cypher-
parameters.html), instead of inserting them in your queries (a little like
prepared statements in SQL). The query will be cached, and if it is sent again
with the same parameters, the execution plan will not be calculated again. To
use them with py2neo, place your dictionary of parameters as the second
argument of query functions.

Teach yourself about the `MERGE` and `CREATE UNIQUE` clauses. Try running the
script above: You can see that there are big differences between variations of
queries, so try to do some benchmarks before. In my case, these clauses were
far slower than a `MATCH` followed by a `CREATE`/`UPDATE`.

There is an equivalent to the `EXPLAIN ANALYZE` of SQL: just put `PROFILE`
before your query to see what it does under the hood.

Read about the indexes (legacy indexes are used to do things like full-text
indexing using lucene, and schema index are like plain indexes in SQL). Using
schema index (or using constraints) on the property of a node can really do
the difference. Maybe, you can store redundant data in a property if it helps
creating a constraint that will ensure your data is clean, and makes access
way faster !

Don’t think too much about reducing the size of the data you store by putting
less into the nodes, concentrate more on the requests you make, the indexes…

There is also a lot of information [in the
documentation](http://neo4j.com/docs/stable/configuration.html), but it is
more about server/OS tuning.

## Deletion¶

If you want to delete all the nodes in your database, it’s best to run :

    
    
    MATCH ()-[r]-() DELETE r
    MATCH (n) DELETE n
    

However, this won’t work if you have a lot of nodes (a million or more),
because it is done in one transaction, and the transactions are kept in
memory.

In that case, the best is to do a `rm -r data/graph.db` in the neo4j data
folder.

See [here](https://zoomicon.wordpress.com/2015/04/18/howto-delete-all-nodes-
and-relationships-from-neo4j-graph-database/) for more information.

Previous: [ Un Firefox qui respecte votre vie privée ](firefox-anonyme.html)
Next: [ Memo with various tips [fr] ](memo.html)

### [palkeo](../index.html)

  * [Projects](../projets/index.html)
  * [Blog articles](index.html)
  * [Links](http://links.palkeo.com)
  * [Repository](http://repo.palkeo.com/)
  * [About](../about.html)

##  06 June 2015

  * Language: [English](language/english.html)

(C)2020, palkeo.

