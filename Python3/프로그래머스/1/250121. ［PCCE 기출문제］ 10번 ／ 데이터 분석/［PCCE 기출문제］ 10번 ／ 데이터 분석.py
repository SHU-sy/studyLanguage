def solution(data, ext, val_ext, sort_by):
    index_dict = {
        "code": 0,
        "date": 1,
        "maximum": 2,
        "remain": 3
    }
    
    ans_data = []
    for d in data:
        if d[index_dict[ext]] < val_ext:
            ans_data.append(d)
    
    return sorted(ans_data, key=lambda x: x[index_dict[sort_by]])