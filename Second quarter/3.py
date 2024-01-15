'''
1.
    a) 0.6
    б) 0.15
    в) 0.87
    г) 0.88 (если я правильно понял опечатку)

2. 
    p(A) = 0.5
    
    а) P(B) = 0.33; P(A∪B) = 1/6
    б) 0.5; 1
    в) 1/6; 1/6
    г) 1/6; 0

3. Код ниже
'''
import matplotlib.pyplot as plt
from matplotlib_venn import venn2, venn3

set_A = {1, 2, 3, 4, 5}
set_B = {3, 4, 5, 6, 7}
set_C = {5, 6, 7, 8, 9}

# Вариант 1: A и B
venn_diagram_AB = venn2([set_A, set_B], set_labels=('A', 'B'))
venn_diagram_AB.get_label_by_id('10').set_text('A - B: 2')
venn_diagram_AB.get_label_by_id('01').set_text('B - A: 2')
venn_diagram_AB.get_label_by_id('11').set_text('A ∩ B: 3')
plt.title('A and B')
plt.show()

# Вариант 2: A и C
venn_diagram_AC = venn2([set_A, set_C], set_labels=('A', 'C'))
venn_diagram_AC.get_label_by_id('10').set_text('A - C: 2')
venn_diagram_AC.get_label_by_id('01').set_text('C - A: 3')
venn_diagram_AC.get_label_by_id('11').set_text('A ∩ C: 2')
plt.title('A and C')
plt.show()

# Вариант 3: B и C
venn_diagram_BC = venn2([set_B, set_C], set_labels=('B', 'C'))
venn_diagram_BC.get_label_by_id('10').set_text('B - C: 2')
venn_diagram_BC.get_label_by_id('01').set_text('C - B: 3')
venn_diagram_BC.get_label_by_id('11').set_text('B ∩ C: 3')
plt.title('B and C')
plt.show()

# Вариант 4: A, B и C
venn_diagram_ABC = venn3([set_A, set_B, set_C], set_labels=('A', 'B', 'C'))
venn_diagram_ABC.get_label_by_id('100').set_text('A - B - C: 0')
venn_diagram_ABC.get_label_by_id('010').set_text('B - A - C: 0')
venn_diagram_ABC.get_label_by_id('001').set_text('C - A - B: 1')
venn_diagram_ABC.get_label_by_id('110').set_text('A ∩ B - C: 2')
venn_diagram_ABC.get_label_by_id('101').set_text('A - B ∩ C: 2')
venn_diagram_ABC.get_label_by_id('011').set_text('B - A ∩ C: 2')
venn_diagram_ABC.get_label_by_id('111').set_text('A ∩ B ∩ C: 3')
plt.title('A, B, and C')
plt.show()

'''
4. 
    а) 0.54
    б) 1 - 0.58 = 0.42

5. 
    а) число кратное 3 также и 6, зависимое событие
    б) независимое событие
'''