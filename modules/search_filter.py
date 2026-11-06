# Search and filtering utilities across services, programs, and inquiries

def search_services(services, keyword):
    if not keyword or not str(keyword).strip():
        return []
    term = str(keyword).strip().lower()
    return [
        s for s in services
        if term in s.service_id.lower()
        or term in s.name.lower()
        or term in s.category.lower()
        or term in s.status.lower()
    ]

def filter_services(services, category=None, status=None):
    results = services
    if category and str(category).strip():
        cat = str(category).strip().lower()
        results = [s for s in results if cat in s.category.lower()]
    if status and str(status).strip():
        st = str(status).strip().lower()
        results = [s for s in results if s.status.lower() == st]
    return results

def search_programs(programs, keyword):
    if not keyword or not str(keyword).strip():
        return []
    term = str(keyword).strip().lower()
    return [
        p for p in programs
        if term in p.program_id.lower()
        or term in p.title.lower()
        or term in p.program_type.lower()
        or term in p.status.lower()
    ]

def filter_programs(programs, program_type=None, status=None):
    results = programs
    if program_type and str(program_type).strip():
        ptype = str(program_type).strip().lower()
        results = [p for p in results if p.program_type.lower() == ptype]
    if status and str(status).strip():
        st = str(status).strip().lower()
        results = [p for p in results if p.status.lower() == st]
    return results

def search_inquiries(inquiries, keyword):
    if not keyword or not str(keyword).strip():
        return []
    term = str(keyword).strip().lower()
    return [
        i for i in inquiries
        if term in i.inquiry_id.lower()
        or term in i.customer_name.lower()
        or term in i.customer_id.lower()
        or term in i.entity_id.lower()
        or term in i.entity_type.lower()
        or term in i.subject.lower()
        or term in i.message.lower()
        or term in i.status.lower()
    ]

def filter_inquiries(inquiries, status=None, entity_type=None):
    results = inquiries
    if status and str(status).strip():
        st = str(status).strip().lower()
        results = [i for i in results if i.status.lower() == st]
    if entity_type and str(entity_type).strip():
        etype = str(entity_type).strip().lower()
        results = [i for i in results if i.entity_type.lower() == etype]
    return results

def universal_search(services, programs, inquiries, keyword):
    if not keyword or not str(keyword).strip():
        return {"services": [], "programs": [], "inquiries": []}
    
    return {
        "services": search_services(services, keyword),
        "programs": search_programs(programs, keyword),
        "inquiries": search_inquiries(inquiries, keyword)
    }
