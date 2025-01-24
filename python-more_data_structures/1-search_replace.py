def search_replace(my_list, search, replace):
    # Utilisation d'une compréhension de liste pour parcourir chaque élément
    # de la liste
    return [
        replace if x == search else x  # Remplacer par 'replace' si l'élément
        # 'x' correspond à 'search', sinon conserver 'x'
        for x in my_list  # Parcourir chaque élément 'x' de la liste 'my_list'
    ]
