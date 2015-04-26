def generate_lesson_title_html(lesson_title):
    title_html = '''
    <div class="lesson">
        ''' + lesson_title
    return title_html


def generate_concept_HTML(concept_title, concept_description):
    html_text_1 = '''
        <div class="concept">
            <div class="concept-title">
                ''' + concept_title
    html_text_2 = '''
            </div>
            <div class="concept-description">
                ''' + concept_description
    html_text_3 = '''
            </div>
        </div>
    '''
    
    full_html_text =  html_text_1 + html_text_2 + html_text_3
    return full_html_text


        

TEST_TEXT = [['Lesson Title 1',[['title 1', 'description1'],
 ['title 2', 'description2'],
 ['title 3', 'description3']]],['Lesson Title 2',[['title 4', 'description4'],
 ['title 5', 'description5'],
 ['title 6', 'description6']]],['Lesson Title 3',[['title 7', 'description7'],
 ['title 8', 'description8'],
 ['title 9', 'description9'],['title 10', 'description10']]]]




def generate_all_html(text):
    all_html = ''
    for item in text:
        lesson = item
        lesson_title = lesson[0]
        lesson_title_html = generate_lesson_title_html(lesson_title)
        all_html = all_html + lesson_title_html
        concepts = lesson[1]
        for concept_number in concepts:
            title = concept_number[0]
            description = concept_number[1]
            concept_html = generate_concept_HTML(title, description)
            all_html = all_html +  concept_html
        all_html = all_html + '''
    </div>'''
    return all_html


print generate_all_html(TEST_TEXT)