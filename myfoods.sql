INSERT INTO public.profile (id, password, last_login, is_superuser, created_at, updated_at, username, email, role, birthdate, profile_pic) VALUES (8, 'pbkdf2_sha256$216000$onAdE017pxqt$OdIiPwj7uRhKh0g01CQE1No/8xdeH/N80WaLMbhuI/A=', '2021-04-24 16:59:17.757787', false, '2021-04-24 16:59:17.635066', '2021-04-24 16:59:17.638566', 'TestUser', 'test@gmail.com', 'user', '2021-04-12', 'woman.jpeg');
INSERT INTO public.profile (id, password, last_login, is_superuser, created_at, updated_at, username, email, role, birthdate, profile_pic) VALUES (7, 'pbkdf2_sha256$216000$HdgI8MOUwVtD$5UkfKsyL94nvwoIGTCUie/bkbx817muQTz7+whJl1+Y=', '2021-04-24 17:19:37.295093', true, '2021-04-24 16:54:37.227241', '2021-04-24 16:54:37.227258', 'Karim', 'karim.valeev.i@gmail.com', 'admin', '2001-05-28', 'cube.jpg');

insert into status(code,name)
values
(111, 'Filling'),
(222,'Paid'),
(205, 'Collecting'),
(333, 'Shipping'),
(202, 'Delivered'),
(555, 'Lost');

insert into category(name)
values
('Dairy products'),
('Meat'),
('Sauces'),
('Grocery'),
('Coffee and tea'),
('Confectionery'),
('Fruits and vegetables'),
('Bread'),
('Frozen food');

insert into shop(site, name, address)
VALUES
       ('https://vk.com/', 'Ашан', 'MSK'),
       ('https://ebay.com', 'Лента', 'KZN'),
       ('https://amazon.com', 'Amazon', 'USA');

INSERT INTO basket (id, name, owner_id, created_at, delivery_address, favourite, status_id) VALUES (10, 'test', 7, '2021-04-06 09:52:36.714918', 'ddd', false, 1);
INSERT INTO basket (id, name, owner_id, created_at, delivery_address, favourite, status_id) VALUES (11, 'dfsgsdfgs', 7, '2021-04-06 09:52:42.204081', 'sdfgsdfgsdfg', true, 1);
INSERT INTO basket (id, name, owner_id, created_at, delivery_address, favourite, status_id) VALUES (12, 'sdfsdf', 7, '2021-04-06 09:56:44.092368', 'fgsdhsdghsg', true, 1);
INSERT INTO basket (id, name, owner_id, created_at, delivery_address, favourite, status_id) VALUES (13, 'sdfgsdfg', 7, '2021-04-06 09:56:47.152903', 'fsfgsdf', false, 1);

INSERT INTO item (id, name, price, icon, amount, kcal, proteins, fats, carbohydrates, category_id, shop_id) VALUES (1, 'milk', 234.01, '', 12, null, null, null, null, 1, 1);
INSERT INTO item (id, name, price, icon, amount, kcal, proteins, fats, carbohydrates, category_id, shop_id) VALUES (2, 'meat', 43, '', 1, null, null, null, null, 2, 1);
INSERT INTO item (id, name, price, icon, amount, kcal, proteins, fats, carbohydrates, category_id, shop_id) VALUES (3, 'Water', 3.99, '', 10000, null, null, null, null, 5, 2);
INSERT INTO item (id, name, price, icon, amount, kcal, proteins, fats, carbohydrates, category_id, shop_id) VALUES (4, 'Tea', 4, '', 23, null, null, null, null, 5, 2);
INSERT INTO item (id, name, price, icon, amount, kcal, proteins, fats, carbohydrates, category_id, shop_id) VALUES (5, 'Melon', 43, '', 4523, null, null, null, null, 7, 3);
INSERT INTO item (id, name, price, icon, amount, kcal, proteins, fats, carbohydrates, category_id, shop_id) VALUES (6, 'Banana', 79.17, '', 666, null, null, null, null, 7, 3);

INSERT INTO sale (id, value, from_date, to_date, item_id) VALUES (1, 0.66, '2021-04-07 08:10:00', '2021-04-22 14:10:00', 1);
INSERT INTO sale (id, value, from_date, to_date, item_id) VALUES (2, 0.39, '2021-04-03 14:10:00', '2021-04-07 14:10:00', 2);
INSERT INTO sale (id, value, from_date, to_date, item_id) VALUES (3, 0.05, '2021-04-19 17:55:00', '2021-04-30 14:10:00', 5);
