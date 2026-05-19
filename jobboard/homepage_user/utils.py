def filterd_objects_with_filter_type(queryset,filter_type):
    if filter_type == "part_time":
        queryset = queryset.filter(employment_type="part_time")
    elif filter_type == "internship":
        queryset = queryset.filter(employment_type="internship")
    elif filter_type == "remote":
        queryset = queryset.filter(employment_type='remote')
    elif filter_type == "without_experience":
        queryset = queryset.filter(experience_required='without_experience')
    return queryset