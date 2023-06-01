:- encoding(utf8).
% Hechos
sintoma(fiebre).
sintoma(tos).
sintoma(dolor_de_pecho).
sintoma(dificultad_respiratoria).
sintoma(fatiga).
sintoma(dolor_de_cabeza).
sintoma(picazon_en_los_ojos).
sintoma(estornudos).
sintoma(secrecion_nasal).
sintoma(congestion_nasal).
sintoma(ronchas_en_la_piel).
sintoma(dolor_de_garganta).
sintoma(nauseas).
sintoma(vomitos).
sintoma(sensibilidad_a_la_luz).
sintoma(sensibilidad_al_ruido).
sintoma(sed_excesiva).
sintoma(miccion_frecuente).
sintoma(hambre_excesiva).
sintoma(perdida_de_peso).
sintoma(sibilancias).
sintoma(opresion_en_el_pecho).
sintoma(dolor_abdominal).
sintoma(acidez_estomacal).
sintoma(debilidad).
sintoma(palidez).
sintoma(falta_de_aire).
sintoma(picazon_en_la_piel).
sintoma(dolor_articular).
sintoma(rigidez_articular).
sintoma(hinchazon_articular).
sintoma(debilidad_muscular).

% hechos - enfermedades
enfermedad(neumonia, [fiebre, tos, dolor_de_pecho, dificultad_respiratoria, fatiga, dolor_de_cabeza]).
enfermedad(alergia, [picazon_en_los_ojos, estornudos, secrecion_nasal, congestion_nasal, ronchas_en_la_piel]).
enfermedad(sinusitis, [dolor_de_cabeza, congestion_nasal, secrecion_nasal, dolor_de_garganta]).
enfermedad(migraña,[dolor_de_cabeza, nauseas, vomitos, sensibilidad_a_la_luz, sensibilidad_al_ruido]).
enfermedad(diabetes, [sed_excesiva, miccion_frecuente, hambre_excesiva, perdida_de_peso]).
enfermedad(asma, [tos, dificultad_respiratoria, sibilancias, opresion_en_el_pecho]).
enfermedad(gastritis, [dolor_abdominal, acidez_estomacal, nauseas, vomitos]).
enfermedad(anemia, [fatiga, debilidad, palidez, dolor_de_cabeza, falta_de_aire]).
enfermedad(insuficiencia_renal, [fatiga, perdida_de_apetito, nauseas, vomitos, picazon_en_la_piel]).
enfermedad(artritis, [dolor_articular, rigidez_articular, hinchazon_articular, debilidad_muscular]).
    
tiene_mitad_mas_1_elementos_comunes(Lista1, Lista2) :-
    num_elementos_comunes(Lista1, Lista2, NumComunes),
    length(Lista1, LongLista1),
    %write("Ingreso "),write(LongLista1),write(" sintomas"),nl,
    length(Lista2, LongLista2),
    %write("Enfermedad a evaluar tiene "),write(LongLista2),write(" sintomas"),nl,
    %write("Sintomas comunes "),write(NumComunes),nl,
    NumComunes >= (LongLista2 // 2) + 1.

%regla base cuando la lista ya esta vacia
num_elementos_comunes([], _, 0).
%regla base cuando es miembro
num_elementos_comunes([H1|T1], L2, N) :-
    member(H1, L2),
    num_elementos_comunes(T1, L2, N1),
    N is N1 + 1.
%regla base cuando no es miembro
num_elementos_comunes([H1|T1], L2, N) :-
    \+ member(H1, L2),
    num_elementos_comunes(T1, L2, N).

enfermedad_sintomas(Sintomas,Enfermedad ) :-
    %write("aca"),
    enfermedad(Enfermedad, ListaSintomas),
    %write("Comparando "), write(Sintomas), write(" con "), write(ListaSintomas), nl,
    tiene_mitad_mas_1_elementos_comunes(Sintomas,ListaSintomas).

enfermedades_coincidentes(Sintomas, Enfermedades) :-
    findall(Enfermedad, enfermedad_sintomas(Sintomas,Enfermedad ), Enfermedades),
    write("e:"),write(Enfermedades).

pregunta([], Lista, Lista).
pregunta([Item|Resto], ListaActual, ListaFinal):-
    format("¿Tiene ~w? (s/n)", Item),
    read(Respuesta),
    (Respuesta == s -> 
        append(ListaActual,[Item],NuevaLista),
        pregunta(Resto, NuevaLista, ListaFinal)
        ;
        pregunta(Resto, ListaActual, ListaFinal)
    ).

contar_elementos([], 0).
contar_elementos([_|T], N) :- contar_elementos(T, N1), N is N1 + 1.

iniciar_inferencia:-
    write("Bienvenido al sistema experto de diagnóstico de enfermedades."), nl,
    write("Por favor, responda las siguientes preguntas con s/n."), nl,
    findall(S, sintoma(S), Sintomas),
    pregunta(Sintomas, [], Lista),write("Eligio:"),write(Lista),nl,
    enfermedades_coincidentes(Lista,EnfermedadesF),
    write("Final: "),nl,write(EnfermedadesF),nl.

