'use strict';
// Class definition

var KTDatatableChildRemoteDataDemo = function() {
	// Private functions

	// demo initializer
	var demo = function() {

		var datatable = $('#kt_datatable').KTDatatable({
			// datasource definition
			data: {
				type: 'remote',
				source: {
					read: {
						url: '/phonebook/deps/',
					},
				},
				pageSize: 10, // display 20 records per page
				serverPaging: true,
				serverFiltering: true,
				serverSorting: true,
			},

			// layout definition
			layout: {
				scroll: false,
				footer: false,
			},

			// column sorting
			sortable: true,

			pagination: false,

			detail: {
				title: 'Просмотр сотрудников',
				content: subTableInit,
			},

			search: {
				input: $('#kt_datatable_search_query'),
				key: 'generalSearch'
			},

			// columns definition
			columns: [
				{
					field: 'RecordID',
					title: '',
					sortable: false,
					width: 30,
					textAlign: 'center',
				}, {
					field: 'name',
					title: 'Название',
					sortable: 'asc',
				}, {
					field: 'region_name',
					title: 'Регион',
				}, {
					field: 'address',
					title: 'Адрес',
				}, {
					field: 'time',
					title: 'Время',
					width: 50,
					textAlign: 'center',
					template: function (row){
									var Data = new Date();
									var Hour = (Data.getUTCHours() + row.time) % 24;
									var Minutes = ('0'+Data.getUTCMinutes()).slice(-2);

									return (Hour + ":" + Minutes);
					},
				},
				{
					field: 'Actions',
					title: 'Действия',
					sortable: false,
					width: 90,
					textAlign: 'center',
					template: function (row){
									return '<a href="mailto:'+row.emails+'"><i class="fas fa-mail-bulk icon-lg" title="Написать всем"></i></a>';
					},
				},
				],
		});

		// $('#kt_datatable_search_status').on('change', function() {
		// 	datatable.search($(this).val().toLowerCase(), 'Status');
		// });

		// $('#kt_datatable_search_type').on('change', function() {
		// 	datatable.search($(this).val().toLowerCase(), 'Type');
		// });
		//
		// $('#kt_datatable_search_status, #kt_datatable_search_type').selectpicker();




		function subTableInit(e) {
			$('<div/>').attr('id', 'child_data_ajax_' + e.data.RecordID).appendTo(e.detailCell).KTDatatable({
				data: {
					type: 'remote',
					source: {
						read: {
							url: '/phonebook/pers/',
							params: {
								// custom query params
								query: {
									generalSearch: '',
									CustomerID: e.data.RecordID,
								},
							},
						},
					},
					pageSize: 5,
					serverPaging: true,
					serverFiltering: false,
					serverSorting: true,
				},

				// layout definition
			layout: {
					scroll: false,
					footer: false,

					// enable/disable datatable spinner.
					spinner: {
						type: 1,
						theme: 'default',
					},
				},

				sortable: true,


				// columns definition
				columns: [
					// {
					// 	field: 'RecordID',
					// 	title: '',
					// 	sortable: false,
					// 	width: 30,
					// },
					{
						field: 'job',
						title: 'Должность',
						width: 70,
					},
					{
						field: 'rank',
						title: 'Звание',
						width: 50,

					},
					{
						field: 'name',
						title: 'ФИО',
						width: 180,

					},   {
						field: 'work_phone',
						title: 'Раб. телефон',
						width: 105,
					}, {
						field: 'cell_phone',
						title: 'Моб. телефон',
						width: 105,

					}, {
						field: 'email',
						title: 'email',
						width: 160,
						template: function (row){
							return '<a href="mailto:'+row.email+'">'+row.email+'</a>'
						}

					},

					{
						field: 'time',
						title: 'Время',
						width: 42,
						template: function (row){
									var Data = new Date();
									var Hour = (Data.getUTCHours() + row.time) % 24;
									var Minutes = ('0'+Data.getUTCMinutes()).slice(-2);

									return (Hour + ":" + Minutes);
					},

					}, {
						field: 'status',
						title: 'Статус',
						width: 100,
						// callback function support for column rendering
						template: function(row) {
							var status = {
								0: {'title': 'На службе', 'class': 'btn-success'},
								1: {'title': 'Болен', 'class': 'btn-warning'},
								2: {'title': 'Коммандировка', 'class': 'btn-primary'},
								3: {'title': 'Отпуск', 'class': 'btn-primary'},
								4: {'title': 'Декрет', 'class': 'btn-info'},
								5: {'title': 'Уволен', 'class': 'btn-info'},
								6: {'title': 'Пенсия', 'class': 'btn-secondary'},
								7: {'title': 'Переведен', 'class': 'btn-secondary'},
							};
							return '<div class="dropdown">\n' +
								'    <button class="btn '+ status[row.status].class +' font-weight-bold btn-sm dropdown-toggle" id="dropdownMenuButton" type="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">\n' +
								status[row.status].title +
								'    </button>\n' +
								//При добавлении нового типа поменять в файле модели Статуса
								'    <div class="dropdown-menu" aria-labelledby="dropdownMenuButton">\n' +
								'        <a class="dropdown-item" href="/phonebook/change_status/'+row.RecordID+'/0/">На службе</a>\n' +
								'        <a class="dropdown-item" href="/phonebook/change_status/'+row.RecordID+'/1/">Болен</a>\n' +
								'        <a class="dropdown-item" href="/phonebook/change_status/'+row.RecordID+'/2/">Коммандировка</a>\n' +
								'        <a class="dropdown-item" href="/phonebook/change_status/'+row.RecordID+'/3/">Отпуск</a>\n' +
								'        <a class="dropdown-item" href="/phonebook/change_status/'+row.RecordID+'/4/">Декрет</a>\n' +
								'        <a class="dropdown-item" href="/phonebook/change_status/'+row.RecordID+'/5/">Уволен</a>\n' +
								'        <a class="dropdown-item" href="/phonebook/change_status/'+row.RecordID+'/6/">Пенсия</a>\n' +
								'        <a class="dropdown-item" href="/phonebook/change_status/'+row.RecordID+'/7/">Переведен</a>\n' +
								'    </div>\n' +

								'</div>';
						},
					},
					// {
					// 	field: 'comment',
					// 	title: 'Комментарий',
					// 	template: function (row){
					// 		return '<div class="dropdown dropdown-inline mr-4">\n' +
					// 			'    <button type="button" class="btn btn-light-primary btn-icon btn-sm" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">\n' +
					// 			'        <i class="ki ki-bold-more-hor"></i>\n' +
					// 			'    </button>\n' +
					// 			'    <div class="dropdown-menu">\n' +
					// 			'        <form class="px-8 py-8" action="/phonebook/change_comment/'+row.RecordID+'/">\n' +
					// 			'            <div class="form-group">\n' +
					// 			'                <label for="exampleDropdownFormPassword1">Комментарий</label>\n' +
					// 			'                <textarea  type="textarea" class="form-control" id="exampleDropdownFormComment" name="comment">'+row.comment+'</textarea>\n' +
					// 			'            </div>\n' +
					// 			'            <button type="submit" class="btn btn-primary">Sign in</button>\n' +
					// 			'        </form>' +
					// 			'    </div>\n' +
					// 			'</div>'
					// 	}
					//
					// },
					// {
						// field: 'Type',
						// title: 'Type',
						// autoHide: false,
						// // callback function support for column rendering
						// template: function(row) {
						// 	var status = {
						// 		1: {'title': 'Online', 'state': 'danger'},
						// 		2: {'title': 'Retail', 'state': 'primary'},
						// 		3: {'title': 'Direct', 'state': 'success'},
						// 	};
						// 	return '<span class="label label-' + status[row.Type].state + ' label-dot mr-2"></span><span class="font-weight-bold text-' +
						// 		status[row.Type].state + '">' +
						// 		status[row.Type].title + '</span>';
						// },
					// },
				// 	{
				// 	field: 'Actions',
				// 	width: 125,
				// 	title: 'Actions',
				// 	sortable: false,
				// 	overflow: 'visible',
				// 	autoHide: false,
				// 	template: function() {
				// 		return '\
	            //             <div class="dropdown dropdown-inline">\
	            //                 <a href="javascript:;" class="btn btn-sm btn-clean btn-icon mr-2" data-toggle="dropdown">\
	            //                     <span class="svg-icon svg-icon-md">\
	            //                         <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="24px" height="24px" viewBox="0 0 24 24" version="1.1">\
	            //                             <g stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">\
	            //                                 <rect x="0" y="0" width="24" height="24"/>\
	            //                                 <path d="M5,8.6862915 L5,5 L8.6862915,5 L11.5857864,2.10050506 L14.4852814,5 L19,5 L19,9.51471863 L21.4852814,12 L19,14.4852814 L19,19 L14.4852814,19 L11.5857864,21.8994949 L8.6862915,19 L5,19 L5,15.3137085 L1.6862915,12 L5,8.6862915 Z M12,15 C13.6568542,15 15,13.6568542 15,12 C15,10.3431458 13.6568542,9 12,9 C10.3431458,9 9,10.3431458 9,12 C9,13.6568542 10.3431458,15 12,15 Z" fill="#000000"/>\
	            //                             </g>\
	            //                         </svg>\
	            //                     </span>\
	            //                 </a>\
	            //                 <div class="dropdown-menu dropdown-menu-sm dropdown-menu-right">\
	            //                     <ul class="navi flex-column navi-hover py-2">\
	            //                         <li class="navi-header font-weight-bolder text-uppercase font-size-xs text-primary pb-2">\
	            //                             Сменить статус:\
	            //                         </li>\
	            //                         <li class="navi-item">\
	            //                             <a href="#" class="navi-link">\
	            //                                 <span class="navi-icon"><i class="la la-print"></i></span>\
	            //                                 <span class="navi-text">Print</span>\
	            //                             </a>\
	            //                         </li>\
	            //                         <li class="navi-item">\
	            //                             <a href="#" class="navi-link">\
	            //                                 <span class="navi-icon"><i class="la la-copy"></i></span>\
	            //                                 <span class="navi-text">Copy</span>\
	            //                             </a>\
	            //                         </li>\
	            //                         <li class="navi-item">\
	            //                             <a href="#" class="navi-link">\
	            //                                 <span class="navi-icon"><i class="la la-file-excel-o"></i></span>\
	            //                                 <span class="navi-text">Excel</span>\
	            //                             </a>\
	            //                         </li>\
	            //                         <li class="navi-item">\
	            //                             <a href="#" class="navi-link">\
	            //                                 <span class="navi-icon"><i class="la la-file-text-o"></i></span>\
	            //                                 <span class="navi-text">CSV</span>\
	            //                             </a>\
	            //                         </li>\
	            //                         <li class="navi-item">\
	            //                             <a href="#" class="navi-link">\
	            //                                 <span class="navi-icon"><i class="la la-file-pdf-o"></i></span>\
	            //                                 <span class="navi-text">PDF</span>\
	            //                             </a>\
	            //                         </li>\
	            //                     </ul>\
	            //                 </div>\
	            //             </div>\
	            //             <a href="javascript:;" class="btn btn-sm btn-clean btn-icon mr-2" title="Edit details">\
	            //                 <span class="svg-icon svg-icon-md">\
	            //                     <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="24px" height="24px" viewBox="0 0 24 24" version="1.1">\
	            //                         <g stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">\
	            //                             <rect x="0" y="0" width="24" height="24"/>\
	            //                             <path d="M8,17.9148182 L8,5.96685884 C8,5.56391781 8.16211443,5.17792052 8.44982609,4.89581508 L10.965708,2.42895648 C11.5426798,1.86322723 12.4640974,1.85620921 13.0496196,2.41308426 L15.5337377,4.77566479 C15.8314604,5.0588212 16,5.45170806 16,5.86258077 L16,17.9148182 C16,18.7432453 15.3284271,19.4148182 14.5,19.4148182 L9.5,19.4148182 C8.67157288,19.4148182 8,18.7432453 8,17.9148182 Z" fill="#000000" fill-rule="nonzero"\ transform="translate(12.000000, 10.707409) rotate(-135.000000) translate(-12.000000, -10.707409) "/>\
	            //                             <rect fill="#000000" opacity="0.3" x="5" y="20" width="15" height="2" rx="1"/>\
	            //                         </g>\
	            //                     </svg>\
	            //                 </span>\
	            //             </a>\
	            //             <a href="javascript:;" class="btn btn-sm btn-clean btn-icon" title="Delete">\
	            //                 <span class="svg-icon svg-icon-md">\
	            //                     <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="24px" height="24px" viewBox="0 0 24 24" version="1.1">\
	            //                         <g stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">\
	            //                             <rect x="0" y="0" width="24" height="24"/>\
	            //                             <path d="M6,8 L6,20.5 C6,21.3284271 6.67157288,22 7.5,22 L16.5,22 C17.3284271,22 18,21.3284271 18,20.5 L18,8 L6,8 Z" fill="#000000" fill-rule="nonzero"/>\
	            //                             <path d="M14,4.5 L14,4 C14,3.44771525 13.5522847,3 13,3 L11,3 C10.4477153,3 10,3.44771525 10,4 L10,4.5 L5.5,4.5 C5.22385763,4.5 5,4.72385763 5,5 L5,5.5 C5,5.77614237 5.22385763,6 5.5,6 L18.5,6 C18.7761424,6 19,5.77614237 19,5.5 L19,5 C19,4.72385763 18.7761424,4.5 18.5,4.5 L14,4.5 Z" fill="#000000" opacity="0.3"/>\
	            //                         </g>\
	            //                     </svg>\
	            //                 </span>\
	            //             </a>\
	            //         ';
				// 	},
				// }
				],
			});
		}
	};

	return {
		// Public functions
		init: function() {
			// init dmeo
			demo();
		},
	};
}();

jQuery(document).ready(function() {
	KTDatatableChildRemoteDataDemo.init();
});
