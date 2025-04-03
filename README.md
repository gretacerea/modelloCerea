Questo progetto sviluppa un modello di regressione per stimare il prezzo al metro quadro di immobili nella zona di Sindian, Nuova Taipei, Taiwan a partire dal dataset "Real Estate Valuation Data Set"
Tale data set contiene dati reali su transazioni immobiliari a Sindian (2012-2013). 
Le colonne più importanti al fine dell'analisi sono:
  - Latitudine, Longitudine
  - Età dell'immobile
  - Distanza dalla stazione MRT più vicina
  - Numero di minimarket nelle vicinanze
  - Prezzo per ping (unità di misura taiwanese che corrisponde al nostro metro quadro)

Per predire il prezzo al metro quadro basandosi su latitudine e longitudine o, in alternativa,su età dell’immobile, distanza dalla stazione MRT più vicina e numero di minimarket 
sono state eseguite due regressioni lineari. I modelli creati sono "model_latlong" (le sue variabili indipendenti sono latitudine e longitudine) e "model_extra" (le sue variabili idipedenti sono età dell'immobile, distanza dalla stazione MRT più vicina,numero di minimarket nelle vicinanze). I codici sono contenuti nei file model.py e modelextra.py

Per eseguire l'applicazione 'Streamlit' scrivere il codice "streamlit run app.py" sul terminale, dovrebbe aprirsi in automatico una finestra nel browser con l’interfaccia dell'applicazione.
In alternativa è possibile accedere manualmente all’indirizzo "http://localhost:8501". 
