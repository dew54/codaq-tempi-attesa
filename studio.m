
%%
[m,n] = size(data) ;
P = 0.02 ;
idx = 1:m %%randperm(m)  ;
sample = EstrazioneVaccini(idx(1:round(P*m)),:) ; 
terzaDose = sample(sample(:,:).serviceName == "Terza Dose", :)
tempiAttesaTerzaDose = seconds(terzaDose.oraServito - terzaDose.oraEmesso)


dataEmissioneTerza = datetime(year(terzaDose.datetimestampIssued), month(terzaDose.datetimestampIssued), day(terzaDose.datetimestampIssued), hour(terzaDose.oraEmesso), minute(terzaDose.oraEmesso), second(terzaDose.oraEmesso)) 
giorno = day(dataEmissioneTerza)
ora = hour(dataEmissioneTerza)
minuto = minute(dataEmissioneTerza)

dataServizioTerza = datetime(year(terzaDose.datetimestampIssued), month(terzaDose.datetimestampIssued), day(terzaDose.datetimestampIssued), hour(terzaDose.oraServito), minute(terzaDose.oraServito), second(terzaDose.oraServito)) 
%%
dayz = weekday(dataEmissioneTerza)
personeInCoda = zeros(length(giorno),1)

% for i = 1:length(giorno)
%     waiting = dataServizioTerza(i) - dataEmissioneTerza(i)
%     for j = 1:length(giorno)
%         
%         if(dataServizioTerza(j) - dataEmissioneTerza(i) < waiting && dataServizioTerza(j) - dataEmissioneTerza(i)>0)
%             personeInCoda (i) = personeInCoda (i) +1
%         end
%     end
% end

for i = 1:610
    personeInCoda (i) = sum(dataServizioTerza(i) > dataServizioTerza) - sum(dataServizioTerza < dataEmissioneTerza(i))
    i
    
end




%%

data = table(dayz, giorno, ora, minuto, tempiAttesaTerzaDose, personeInCoda)
%%
[m,n] = size(data) ;
P = 0.70 ;
idx = randperm(m)  ;
training = data(idx(1:round(P*m)),:) ; 
testing = data(idx(round(P*m)+1:end),:) ;

%%

Mdl = fitrnet(training,"tempiAttesaTerzaDose","Standardize",true)
%%
testMSE = loss(Mdl,testing,"tempiAttesaTerzaDose")
testPredictions = predict(Mdl,testing);

plot(testing,testPredictions,".")
hold on
plot(YTest,YTest)
hold off
xlabel("True MPG")
ylabel("Predicted MPG")


