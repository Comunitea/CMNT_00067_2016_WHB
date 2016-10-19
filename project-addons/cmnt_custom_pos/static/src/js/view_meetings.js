function openerp_custom_view_meetings(instance, module){
    var QWeb = instance.web.qweb;
	var _t = instance.web._t;

    module.ViewMeetingScreenWidget = module.ScreenWidget.extend({
        template: 'ViewMeetingScreenWidget',

        show_leftpane: false,
        previous_screen: 'products',

        init: function(parent, options) {
            this._super(parent,options);
            this.events = [];
        },
        show: function(){
            var self = this;
            this._super();
            this.renderElement();

            // Funcionality of back button
            this.$('.back').click(function(){
                self.pos_widget.screen_selector.set_current_screen(self.previous_screen);
            });

            // Get and show meetings in a list
            $.when(this.get_events()).done(function(){
                self.show_events()
            });
        },
        fetch: function(model, fields, domain, order, ctx){
            return new instance.web.Model(model).query(fields).filter(domain).order_by(order).context(ctx).all()
        },
        get_events: function(){

            var self=this;
            var model = 'calendar.event'
            var fields = ['name', 'display_start', 'start_date', 'stop_date', 'start_datetime', 'stop_datetime']
            var client = this.pos.get('selectedOrder').get('client');
            var order = "display_start"
            console.log("CLIENTE")
            console.log(client)
            var today = new Date()
            var today3 = new Date();
            today3.setMonth(today3.getMonth() + 3)
            var start_date = $.datepicker.formatDate('yy-mm-dd', today);
            var end_date = $.datepicker.formatDate('yy-mm-dd', today3);

            var domain = [
                ['display_start', '>=', start_date + " 00:00:00"],
                ['display_start', '<=', end_date +  " 23:59:59"],
            ]
            if (client) {
                domain.push(['partner_ids', 'in', [client.id]])
            }
            console.log("DOMAIN")
            console.log(domain)
            var loaded = self.fetch(model, fields, domain, order).then(function(events){

                self.events = events
            });
            return loaded;

        },
        show_events: function(){
            var contents = this.$el[0].querySelector('.event-list-contents');
            contents.innerHTML = "";
            for(var i = 0, len = Math.min(this.events.length,100); i < len; i++){
                var event = this.events[i];
                console.log("EVENTS")
                var eventline_html = QWeb.render('EventLine',{widget: this, event:event});
                var eventline = document.createElement('tbody');
                eventline.innerHTML = eventline_html;
                eventline = eventline.childNodes[1];
                contents.appendChild(eventline);
            }
        },
        format_date: function(date){
            var format_date = date
            var splited_date = date.split(" ")
            var to_format = splited_date[0]
            var splited_to_format = to_format.split("-")
            format_date = splited_to_format[2] + "-" +splited_to_format[1] + "-" +splited_to_format[0]
            if (splited_date.length === 2){
                format_date = format_date + "  " + splited_date[1]
            }
            return format_date 
        }
    });

    module.PosWidget.include({
        build_widgets: function(){
            var self = this;
            this._super();

            // Add View Meetings Buttom, Lo comenté poruqe no quieren las citas
            var view_meeting = $(QWeb.render('ViewMettingButton'));
            view_meeting.appendTo(this.$('.pos-rightheader'));

            // Add Meetings Screen
            this.view_meeting_screen = new module.ViewMeetingScreenWidget(this, {});
            this.view_meeting_screen.appendTo(this.$('.screens'));
            this.screen_selector.add_screen('view_meeting', this.view_meeting_screen);

            // Link screen to click in Button
            view_meeting.click(function(){
                self.pos_widget.screen_selector.set_current_screen('view_meeting');
            });
            
        },
    });

    // Para ocultar el botón de modificar el precio
    module.NumpadWidget = module.NumpadWidget.extend({
        start: function(){
            var self = this;
            this._super();
            this.$el.find("button[data-mode='price']").css('visibility', 'hidden')
        },
       
    });
}
