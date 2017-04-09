

docker cp sms_data.csv hackathonredash:/tmp/sms_data.csv
docker cp encaminhamento_data.csv hackathonredash:/tmp/encaminhamento_data.csv
docker cp stabsus_data.csv hackathonredash:/tmp/stabsus_data.csv


CREATE TABLE sms (
    ouvidoria_atendimento_demanda text,
    numero_do_protocolo text,
    numero_do_atendimento text,
    data_atendimento text,
    meio_atendimento text,
    classificacao text,
    status_da_demanda text,
    data_do_assunto text,
    assunto text,
    subassunto_1 text,
    subassunto_2 text,
    subassunto_3 text,
    farmaco text,
    d_a_p_s text,
    data_de_conclusao_efetiva text,
    hora_de_conclusao_efetiva text,
    prazo_vencido text,
    data_de_conclusao_prevista text,
    sexo_do_referido text,
    idade_do_referido text,
    origem_do_documento text,
    id_do_tecnico text,
    tecnico_ativo text,
    primeiro_destino_encaminhamento text,
    data_primeiro_destino_encaminhamento text,
    municipio_primeiro_destino_encaminhamento text,
    uf_primeiro_destino_encaminhamento text,
    acesso_atual text,
    destino_atual text,
    municipio_atual text,
    ultimo_destino text,
    municipio_ultima text,
    acesso_ultima text,
    data_do_ultimo_destino text,
    imediato text,
    demanda_ativa text,
    atendimento_finalizado text,
    estabelecimento_comercial text,
    sigilo text,
    anonimo text
);

LOAD DATA INFILE '/tmp/sms_data.csv'
INTO TABLE sms
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;



CREATE TABLE encaminhamento(
    ouvidoria_atendimento_demanda text,
    numero_do_protocolo text,
    numero_do_atendimento text,
    data_atendimento text,
    meio_atendimento text,
    classificacao text,
    status_da_demanda text,
    data_do_assunto text,
    assunto text,
    subassunto_1 text,
    subassunto_2 text,
    subassunto_3 text,
    farmaco text,
    d_a_p_s text,
    data_de_conclusao_efetiva text,
    hora_de_conclusao_efetiva text,
    prazo_vencido text,
    data_de_conclusao_prevista text,
    sexo_do_referido text,
    idade_do_referido text,
    origem_do_documento text,
    id_do_tecnico text,
    tecnico_ativo text,
    data_primeiro_destino_encaminhamento text,
    uf_primeiro_destino_encaminhamento text,
    municipio_primeiro_destino_encaminhamento text,
    primeiro_destino_encaminhamento text,
    acesso_atual text,
    destino_atual text,
    municipio_atual text,
    ultimo_destino text,
    municipio_ultima text,
    acesso_ultima text,
    data_do_ultimo_destino text,
    imediato text,
    demanda_ativa text,
    atendimento_finalizado text,
    estabelecimento_comercial text,
    sigilo text,
    anonimo text
);

LOAD DATA INFILE '/tmp/encaminhamento_data.csv'
INTO TABLE encaminhamento
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;



CREATE TABLE stabsus(
    crs__coordenadoria_regional_de_saude text,
    pr__prefeitura_regional text,
    sts__supervisao_tecnica_de_saude text,
    da_distrito_administrativo text,
    n0_cnes__cadastro_nacional_de_estabelecimentos_de_saude text,
    nome_do_estabelecimento text,
    tipo_de_servico text,
    tipo_gerenciamento text,
    nome_instituicao_gerenciamento text,
    logradouro text,
    n0 text,
    cep text,
    bairro text,
    fone_1 text,
    fone_2 text,
    x_utm_mdc text,
    y_utm_mdc text,
    latitudegoogle text,
    longitudegoogle text,
    latitudemdc text,
    longitudemdc text,
    horario_de_funcionamento text
);

LOAD DATA INFILE '/tmp/stabsus_data.csv'
INTO TABLE stabsus
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

