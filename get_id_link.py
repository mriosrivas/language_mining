def get_id_link(id='prensalibregt/posts?'):
    post = graph.get_object(id=id, fields='link')
    id_news = []
    link_news = []
    
    for posts in post['data']:
        id_news.append(posts['id'])
        link_news.append(posts['link'])
        #print(posts)
    return [id_news,  link_news]   
        
[id_news,  link_news] = get_id_link()
