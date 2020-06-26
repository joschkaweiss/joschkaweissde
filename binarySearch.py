def binaersuche_rekursiv(werte, gesucht, start, ende):
    if ende < start:
        return 'nicht gefunden'
        
    mitte = (start + ende) // 2
    if werte[mitte] == gesucht:
        return mitte
    elif werte[mitte] < gesucht:
        return binaersuche_rekursiv(werte, gesucht, mitte + 1, ende)
    else:
        return binaersuche_rekursiv(werte, gesucht, start, mitte - 1)
   
 def binaersuche(werte, gesucht):
    return binaersuche_rekursiv(werte, gesucht, 0, len(werte) - 1)
