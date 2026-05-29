from django import forms
from .models import Alumnos, Curso, NotasAlumnosPorCurso

class NotasForm(forms.ModelForm):
    cui_alumno = forms.CharField(max_length=8, label="CUI del alumno")
    id_curso = forms.IntegerField()
    class Meta:
        model = NotasAlumnosPorCurso
        fields = ['cui_alumno', 'id_curso', 'nota']
    def clean_cui_alumno(self):
        cui = self.cleaned_data.get('cui_alumno')
        if not Alumnos.objects.filter(cui = cui).exists():
            raise forms.ValidationError("No existe un alumno con este CUI")
        return cui
    def clean_id_curso(self):
        id_c = self.cleaned_data.get('id_curso')
        if not Curso.objects.filter(id_curso = id_c).exists():
            raise forms.ValidationError("No existe curso con ese id")
        return id_c
    def save(self, commit = True):
        cui = self.cleaned_data.get('cui_alumno')
        alumno = Alumnos.objects.get(cui = cui)
        id_c = self.cleaned_data.get('id_curso')
        curso = Curso.objects.get(id_curso = id_c)
        registro = super().save(commit=False)
        registro.alumno = alumno
        registro.curso = curso
        if commit:
            registro.save()
        return registro
              