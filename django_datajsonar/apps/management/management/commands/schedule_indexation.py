#! coding: utf-8
import logging
import datetime

from scheduler.models import RepeatableJob
from django.core.management import BaseCommand
from django.utils.timezone import now

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    """Comando para ejecutar la indexación manualmente de manera sincrónica,
    útil para debugging. No correr junto con el rqscheduler para asegurar
    la generación de reportes correcta."""

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='The name for the repeatable job')

        parser.add_argument('-c', '--callable', type=str,
                            help='importable method to be called',
                            default='django_datajsonar.libs.indexing.tasks.schedule_new_read_datajson_task')

        parser.add_argument('-t', '--time', nargs=2,
                            help='UTC hour and minutes to schedule first job, default: 6:00am',
                            metavar=('HOURS', 'MINUTES'),
                            default=[6, 0]
                            )

        parser.add_argument('-i', '--interval', nargs=2,
                            help='interval and unit in which to repeat the job, default: 24 hours',
                            metavar=('UNIT', '[weeks|days|hours|minutes]'),
                            default=[24, 'hours']
                            )

    def handle(self, *args, **options):
        # chequear que no haya un trabajo scheduleado previo
        method = options['callable']
        interval = options['interval']
        previously_scheduled_jobs = RepeatableJob.objects.filter(callable=method,
                                                                 interval=int(interval[0]),
                                                                 interval_unit=interval[1])

        if previously_scheduled_jobs:

            self.stdout.write(u'Ya hay un RepeatableJob registrado con ese metodo e intervalo')
            return

        start_time = now() + datetime.timedelta(days=1)
        time = map(int, options['time'])
        start_time = start_time.replace(hour=time[0],
                                        minute=time[1],
                                        second=0,
                                        microsecond=0)

        RepeatableJob.objects.update_or_create(
            name=options['name'],
            defaults={
                'callable': method,
                'queue': 'indexing',
                'scheduled_time': start_time,
                'interval': int(interval[0]),
                'interval_unit': interval[1],
                'repeat': None
            })

